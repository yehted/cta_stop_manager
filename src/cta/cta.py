import pandas

class StopRouteManager(object):
    def __init__(self, df):
        self.df = df
        self.stop_route_df = self._get_normalized_route_stops()

    def _get_normalized_route_stops(self):
        """ Creates a normalized table for easier access """
        df = self.df.set_index('stop_id')
        stop_route_df = df['routes'].str.split(',', expand=True)
        stop_route_df = stop_route_df.stack().reset_index()
        stop_route_df = stop_route_df.rename(columns={0: 'route'})
        stop_route_df = stop_route_df.drop('level_1', axis=1)

        return stop_route_df

    def get_longest_route(self):
        """ Return the route that has the most stops """
        stop_count = self.stop_route_df.groupby('route').count()

        return stop_count.idxmax().iloc[0]

    def get_busiest_stop(self):
        """ Return the stop_id that has the most routes servicing it """
        route_count = self.stop_route_df.groupby('stop_id').count()

        return route_count.idxmax().iloc[0]

    def get_street_with_most_stops(self):
        """ Return the name of the on_street that has the most stops """
        stop_count = self.df.groupby('on_street').count()

        return stop_count.idxmax().iloc[0]

def get_data():
    """ This should read the csv and return an unprocessed DataFrame """
    pass


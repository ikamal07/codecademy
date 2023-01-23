import pickle

movie_dataset = pickle.load( open( "movie_regression_dataset.p", "rb" ) )
movie_ratings = pickle.load( open( "movie_regression_labels.p", "rb" ) )

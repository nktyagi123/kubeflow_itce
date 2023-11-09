import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SpatialDropout1D, LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping

def train_lstm_model(X_train, Y_train, embedding_dim=100, epochs=10, batch_size=64, early_stopping_patience=3):
    # Your LSTM model training logic here
    pass

if __name__ == "__main__":
    # You can add command-line argument parsing for 'X_train', 'Y_train', 'embedding_dim', 'epochs', 'batch_size', and 'early_stopping_patience' here
    # Call your train_lstm_model function with the necessary arguments
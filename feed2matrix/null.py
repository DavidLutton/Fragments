import pickle

delta = 'entries.pickle'
with open(delta, 'wb') as f:
    entries = []
    pickle.dump(entries, f, pickle.HIGHEST_PROTOCOL)

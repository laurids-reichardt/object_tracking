# %%
import pickle

with open ('tracked_boxes.pickle', 'rb') as fp:
    tracked_bboxes = pickle.load(fp)

print(tracked_bboxes)
# %%

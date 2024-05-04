# # model hyperparameters
# encoder_checkpoint = 'distilbert/distilbert-base-uncased' # 'google-bert/bert-base-uncased', 'distilbert/distilbert-base-uncased'
# hidden_dropout_prob = 0.2
# modality_att_dropout_prob = 0.1
# hidden_size = 768 # depends on chosen encoder
# projection_size = 30
# num_labels = 1

# # training arguments
# batch_size = 8
# num_epochs = 3
# criterion = 'maeloss'# ['crossentropyloss', 'mseloss', 'maeloss', '']
# optimizer = 'adamw' # ['adamw', 'adam', 'rmsprop'] 'adadelta'
# lr = 2e-5
# scheduler_type = 'linear'
# num_warmup_steps = 0
# best_model_metric = 'mse' # 'accuracy' ['accuracy', 'mse', 'pearsonr', 'mae', 'loss']
# save_best_model = True


# model hyperparameters
encoder_checkpoint = 'distilbert/distilbert-base-uncased' # 'google-bert/bert-base-uncased' # 'distilbert/distilbert-base-uncased'
hidden_dropout_prob = 0.2 # check value in paper / github default
modality_att_dropout_prob = 0.3 # paper value
hidden_size = 768 # depends on chosen encoder
projection_size = 30 #
num_labels = 2 # [1, 2, 7]

# training arguments
batch_size = 24 # [8, 24], 24 - 
num_epochs = 3
criterion = 'crossentropyloss'# ['crossentropyloss', 'mseloss', 'maeloss', '']
optimizer = 'adamw' # ['adamw', 'adam', 'rmsprop'] 'adadelta'
lr = 2e-5 # 
scheduler_type = 'linear' # ['linear', 'constant', 'cosine', 'cosine_with_restarts', 'polynomial', 'constant', 'constant_with_warmup', 'inverse_sqrt', 'reduce_lr_on_plateau', 'cosine_with_min_lr', 'warmup_stable_decay']
warmup_steps_ratio = 0.1 #
best_model_metric = 'accuracy' # 'accuracy' ['accuracy', 'mse', 'pearsonr', 'loss']
save_best_model = False
save_model_dest = 'models/'

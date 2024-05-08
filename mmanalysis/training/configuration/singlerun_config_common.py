# model hyperparameters
encoder_checkpoint = 'distilbert/distilbert-base-uncased' # 'google-bert/bert-base-uncased' # 'distilbert/distilbert-base-uncased'
hidden_dropout_prob = 0.2 # 
modality_att_dropout_prob = 0.3 # paper value
hidden_size = 768 # depends on chosen encoder
projection_size = 768 #
num_labels = 2 # [1, 2, 7]

# training arguments
batch_size = 8 # [8, 24], 24 - 
num_epochs = 3
chunk_size = None
criterion = 'crossentropyloss'# ['crossentropyloss', 'mseloss', 'maeloss', '']
optimizer = 'adamw' # ['adamw', 'adam', 'rmsprop'] 'adadelta'
lr = 5e-5 # 
scheduler_type = 'linear' # ['linear', 'constant', 'cosine', 'cosine_with_restarts', 'polynomial', 'constant', 'constant_with_warmup', 'inverse_sqrt', 'reduce_lr_on_plateau', 'cosine_with_min_lr', 'warmup_stable_decay']
warmup_steps_ratio = 0.0 #
best_model_metric = 'accuracy' # 'accuracy' ['accuracy', 'mse', 'pearsonr', 'loss']
save_best_model = False
save_model_dest = 'models/'
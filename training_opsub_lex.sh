MONO_DATASET='en:./data/OpSub-LEX/en.train.pth,,;hi:./data/OpSub-LEX/hi.train.pth,,'
PARA_DATASET='en-hi:,./data/OpSub-LEX/XX.valid.pth,./data/OpSub-LEX/XX.test.pth'
PRETRAINED='./data/all.256.vec'

#CUDA_VISIBLE_DEVICES=0 
python3 main.py \
--exp_name training_opsub_lex \
--transformer True \
--n_enc_layers 3 \
--n_dec_layers 3 \
--share_enc 2 \
--share_dec 2 \
--share_lang_emb True \
--share_output_emb True \
--emb_dim 256 \
--langs 'en,hi' \
--n_mono -1 \
--mono_dataset $MONO_DATASET \
--para_dataset $PARA_DATASET \
--mono_directions 'en,hi' \
--pivo_directions 'en-hi-en,hi-en-hi' \
--word_shuffle 3 \
--word_dropout 0.1 \
--word_blank 0.2 \
--pretrained_emb $PRETRAINED \
--pretrained_out True \
--lambda_xe_mono 1 \
--lambda_xe_otfd 1 \
--otf_num_processes 30 \
--otf_sync_params_every 1000 \
--enc_optimizer adam,lr=0.0001 \
--group_by_size True \
--batch_size 16 \
--epoch_size 200000 \
--stopping_criterion bleu_en_hi_en_valid,50 \
--freeze_enc_emb False \
--freeze_dec_emb False \
--reload_model dumped/pretraining_step/best-bleu_en_hi_valid.pth \
--reload_enc True \
--reload_dec True

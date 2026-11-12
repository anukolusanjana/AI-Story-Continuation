# Run from the project root after installing torch-model-archiver.
python scripts/download_model.py
New-Item -ItemType Directory -Force model-store | Out-Null
torch-model-archiver --model-name story_generator --version 1.0 `
  --serialized-file model_files/pytorch_model.bin `
  --handler handler.py `
  --extra-files "model_files/config.json,model_files/generation_config.json,model_files/tokenizer.json,model_files/tokenizer_config.json,model_files/special_tokens_map.json,model_files/vocab.json,model_files/merges.txt" `
  --export-path model-store --force
Write-Host "Created model-store/story_generator.mar"

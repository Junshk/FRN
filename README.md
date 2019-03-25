## FRN (Fractal Residual Network)

## Dependencies

* PyTorch 1.0.0

## Code 

# Test

For test submission,

0. Prepare dataset in some folder 'data_path'
You should have the following directory structure:
`data_path/val/cam*_0*.png`

1. Download [Model](https://drive.google.com/open?id=16uLTctvej3SqgdBeKl5BA7G3luSF9QmP)
2. Type following command.

```bash 
python main.py --pre_train 'model_path' --test_only --self_ensemble --save_results --dir_data 'data_path' --n_val 10 --data_test NTIRE_VAL
```

3. The result images will be saved in 'experiment/test/results' folder.

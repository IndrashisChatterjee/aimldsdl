# Knowledge Distillation on MNIST

This project demonstrates knowledge distillation using PyTorch on the MNIST dataset. A larger "teacher" model is trained first, and its knowledge is transferred to a smaller "student" model using KL divergence loss.

## Structure

- `kd/knowledge_distillation.ipynb`: Main Jupyter notebook containing all code for training, evaluation, and distillation.

## Usage

1. Open `kd/knowledge_distillation.ipynb` in Jupyter or VS Code.
2. Run all cells to:
   - Train the teacher model.
   - Train the student model using knowledge distillation.
   - Evaluate both models.

## Requirements

- Python 3
- PyTorch
- torchvision
- numpy
- pandas
- tqdm

Install dependencies with:

```sh
pip install torch torchvision numpy pandas tqdm
```

## Results

- Teacher model achieves high accuracy on MNIST.
- Student model learns from teacher and achieves competitive accuracy with fewer parameters.

## References
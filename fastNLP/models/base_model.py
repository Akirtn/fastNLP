import torch

from fastNLP.modules.decoder.MLP import MLP


class BaseModel(torch.nn.Module):
    """Base PyTorch model for all models.
    """

    def __init__(self):
        super(BaseModel, self).__init__()

    def fit(self, train_data, dev_data=None, **train_args):
        pass

    def predict(self, *args, **kwargs):
        raise NotImplementedError


class NaiveClassifier(BaseModel):
    def __init__(self, in_feature_dim, out_feature_dim):
        super(NaiveClassifier, self).__init__()
        self.mlp = MLP([in_feature_dim, in_feature_dim, out_feature_dim, out_feature_dim])
        self.softmax = torch.nn.Softmax(dim=0)

    def forward(self, x):
        return {"predict": self.softmax(self.mlp(x))}

    def predict(self, x):
        return {"predict": self.softmax(self.mlp(x))}

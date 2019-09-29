#  Tencent is pleased to support the open source community by making GNES available.
#
#  Copyright (C) 2019 THL A29 Limited, a Tencent company. All rights reserved.
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


from gnes.encoder.text.transformer import PyTorchTransformers


class DistilBertEncoder(PyTorchTransformers):
    def post_init(self):
        self.model_name = 'distilbert-base-uncased'

        from pytorch_transformers import DistilBertModel, DistilBertTokenizer
        # select the model, tokenizer & weight accordingly
        model_class, tokenizer_class, pretrained_weights = DistilBertModel, DistilBertTokenizer, 'distilbert-base-uncased'

        def load_model_tokenizer(x):
            return model_class.from_pretrained(x).eval(), tokenizer_class.from_pretrained(x)

        try:
            self.model, self.tokenizer = load_model_tokenizer(self.work_dir)
        except Exception:
            self.logger.warning('cannot deserialize model/tokenizer from %s, will download from web' % self.work_dir)
            self.model, self.tokenizer = load_model_tokenizer(pretrained_weights)

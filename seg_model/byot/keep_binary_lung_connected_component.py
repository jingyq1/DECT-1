import numpy as np
from skimage import measure
from ai4med.common.medical_image import MedicalImage
from ai4med.common.transform_ctx import TransformContext
from ai4med.components.transforms.transformer import Transformer


class KeepBinaryLungCC(Transformer):
    def __init__(self, field='model', min_size=0, min_ratio=0):
        Transformer.__init__(self)
        self._field = field
        self._min_size = min_size
        self._min_ratio = min_ratio

    def keep_lung_cc(self, nda):
        labels = measure.label(nda > 0)
        if labels.max() != 0:
            stat_cc = np.bincount(labels.flat)[1:]
            idx_cc = np.argsort(-stat_cc)
            size_1 = stat_cc[idx_cc[0]]
            size_2 = stat_cc[idx_cc[1]]
            #print(size_1, size_2)
            lung_cc = (labels == idx_cc[0] + 1)
            if size_2 > self._min_size and size_2 > size_1 * self._min_ratio:
                lung_cc = lung_cc + (labels == idx_cc[1] + 1)
            lung_cc = lung_cc.astype(nda.dtype)
        else:
            lung_cc = np.zeros(shape=nda.shape, dtype=nda.dtype)
        return lung_cc

    def transform(self, transform_ctx: TransformContext):

        image_in = transform_ctx.get_image(self._field)
        volume = image_in.get_data()
        output = volume

        foreground = (volume == 1).astype(np.uint8)
        mask = self.keep_lung_cc(foreground)
        output = mask * volume

        m = image_in.new_image(output, image_in.get_shape_format())

        transform_ctx.set_image(self._field, m)
        return transform_ctx

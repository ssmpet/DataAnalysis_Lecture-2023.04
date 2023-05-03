import numpy as np
import matplotlib.pyplot as plt
import os

def sub_scatter(num, xmean, xstd, ymin, ymax, app):
    colors = np.random.rand(100)

    xs = np.random.normal(loc=xmean, scale=xstd, size=num)
    ys = np.random.uniform(ymin, ymax, num)

    # figure 를 꼭 써 주어야 함. 새로운 객체 생성
    plt.figure()
    plt.scatter(xs, ys, c=colors, alpha=0.8)
    filename = os.path.join(app.static_folder, 'img/scatter.png')
    plt.savefig(filename)
    mtime = int(os.stat(filename).st_mtime)   # 마지막으로 변경된 시간

    return mtime
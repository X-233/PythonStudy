# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    G = nx.Graph()  # 无向图
    # 添加节点
    G.add_nodes_from([1, 2, 3, 4])
    # 添加节点
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

    # 可视化
    nx.draw(G, with_labels=True)
    plt.show()

    # 获取图的邻阶矩阵
    As = nx.adjacency_matrix(G)
    print(As)

    # 转成二维矩阵, 邻接矩阵
    A = As.todense()

    # 转成, dna

    # 表示是否
    print(A)
    B = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    B_g = nx.from_numpy_matrix(B)
    nx.draw(B_g, node_size=500, with_labels=True)
    plt.show()


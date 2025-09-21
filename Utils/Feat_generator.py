def vec_generator(file):
    import pandas as pd
    import numpy as np
    import node2vec
    import  networkx as nx
    from sklearn.decomposition import PCA
    params = {
        "dimensions": 128,
        "walk_length": 30,
        "num_walks": 200,
        "window": 10,
        "min_count": 1
    }
    print("Processing: ", file)
    adj_matrix = pd.read_parquet(f"../Adj_Matrices/{file}.parquet")
    graph = nx.DiGraph(adj_matrix)
    node2vec1 = node2vec.Node2Vec(graph,dimensions=params["dimensions"],walk_length=params["walk_length"],num_walks=params["num_walks"],workers=4)
    model=node2vec1.fit(window=params["window"],min_count=params["min_count"])
    graph_embeddings={node: model.wv[node] for node in graph.nodes()}
    graph_embeddings=np.array([val for val in graph_embeddings.values()])
    pca = PCA(n_components=1)
    graph_embeddings_pca=pca.fit_transform(graph_embeddings)
    graph_embeddings_array=np.array(graph_embeddings_pca)
    graph_embeddings_array.resize((1,37433))
    df=pd.DataFrame(graph_embeddings_array,columns=[f"Feat_{vec}" for vec in range(1,37434)])
    df.to_parquet(f'../Features/{file}.parquet',index=False)
    print('Completed: ', file)
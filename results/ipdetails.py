import pandas as pd

def print_table(df:pd.DataFrame) -> None:
    
    df_tiny = df[(df['nodes'] <= 25)]
    df_medium = df[(df['nodes'] > 25) & (df['nodes'] <= 100)]
    df_large = df[(df['nodes'] > 100) & (df['nodes'] <= 250)]
    df_jumbo = df[(df['nodes'] > 250)]

    print("Class, N, nodes, arcs, rounds, numinitialcuts, numtotalcuts, IPNodes, IPTime, SepTime")
    
    print(f"Tiny, {df_tiny.shape[0]}, {df_tiny['nodes'].mean()}, {df_tiny['arcs'].mean()}, {df_tiny['iteration'].mean()}, {df_tiny['initialTrianglesSize'].mean()}, {df_tiny['TotalNumCuts'].mean()}, {df_tiny['TotalNumNodes'].mean()}, {df_tiny['totalIpTime'].mean()}, {df_tiny['totalTriangleTime'].mean()}")
    
    print(f"Medium, {df_medium.shape[0]}, {df_medium['nodes'].mean()}, {df_medium['arcs'].mean()}, {df_medium['iteration'].mean()}, {df_medium['initialTrianglesSize'].mean()}, {df_medium['TotalNumCuts'].mean()}, {df_medium['TotalNumNodes'].mean()}, {df_medium['totalIpTime'].mean()}, {df_medium['totalTriangleTime'].mean()}")

    print(f"Large, {df_large.shape[0]}, {df_large['nodes'].mean()}, {df_large['arcs'].mean()}, {df_large['iteration'].mean()}, {df_large['initialTrianglesSize'].mean()}, {df_large['TotalNumCuts'].mean()}, {df_large['TotalNumNodes'].mean()}, {df_large['totalIpTime'].mean()}, {df_large['totalTriangleTime'].mean()}")

    print(f"Jumbo, {df_jumbo.shape[0]}, {df_jumbo['nodes'].mean()}, {df_jumbo['arcs'].mean()}, {df_jumbo['iteration'].mean()}, {df_jumbo['initialTrianglesSize'].mean()}, {df_jumbo['TotalNumCuts'].mean()}, {df_jumbo['TotalNumNodes'].mean()}, {df_jumbo['totalIpTime'].mean()}, {df_jumbo['totalTriangleTime'].mean()}")

    # This is just to see the final separation times:
    # print (f"{df_tiny['triangleTime_lf'].mean()}, {df_medium['triangleTime_lf'].mean()}, {df_large['triangleTime_lf'].mean()}, {df_jumbo['triangleTime_lf'].mean()}")
    



def main() -> None:

    lc = pd.read_csv('lemon-coarse.csv')
    # Just do for trial 1; results don't differ for the same app/version run
    lc = lc[lc['trial']==1]
    lc.drop(columns='trial', inplace=True)

    lf = pd.read_csv('lemon-fine.csv')
    # Just do for trial 1; results don't differ for the same app/version run
    lf = lf[lf['trial']==1]
    lf.drop(columns='trial', inplace=True)

    key = ['application','version','instrumentor','function']
    lc.set_index(key, inplace=True)
    lf.set_index(key, inplace=True)
    jdf = lc.join(lf, on=key, lsuffix='_lc', rsuffix='_lf')
    jdf = jdf.drop(columns=['maxIterations', 'initialMaxDepth','maxDepthIncrement','finalMaxDepth', 'numProbe', 'objectiveValue', 'zip', 'depth'])

    sumdf = jdf.groupby(by=key).sum()
    maxdf = jdf.groupby(by=key).max()

    df = pd.DataFrame([maxdf.nodes, maxdf.arcs, maxdf.initialTrianglesSize, sumdf.tSize, maxdf.iteration, sumdf.numNodes, maxdf.totalIpTime, maxdf.totalTriangleTime, maxdf.triangleTime_lf]).transpose()

    df['TotalNumNodes'] = df['iteration'] + df['numNodes']
    df['TotalNumCuts'] = df['initialTrianglesSize'] + df['tSize']
    df['TotalBaseTime'] = df['totalIpTime'] + df['totalTriangleTime']

    print_table(df)


if __name__ == '__main__':
    main()


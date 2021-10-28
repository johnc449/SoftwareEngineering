public class LCA {
	private int V;
	private int E;
	private int[][] adj;
	private int[] odegree;
	private int[] idegree;

	// initialises empty graph with v vertices
	public LCA(int V) {
		this.V = V;
		this.E = 0;
		idegree = new int[V];
		odegree = new int[V];
		adj = new int[V][V];
		for (int i = 0; i < V; i++) {
			for (int j = 0; j < V; j++) {
				adj[i][j] = 0;
			}
		}
	}

	public void addEdge(int v, int w){
	    adj[v][w]=1;
	    idegree[w]++;
	    odegree[v]++;
	    E++;
    }
	public int LCAFind(int v, int w) {
		int vCount = 0;
		int wCount = 0;
		boolean[] vMarked = new boolean[V];
		boolean[] wMark = new boolean[V];
		int[] verticesArray = new int[E];
		int[] wArray = new int[E];
		
		verticesArray[vCount] = v;
		wArray[wCount] = w;
		for (int j = 0; j < V; j++) {// marks vertices as not visited
			vMarked[j] = false;
			wMark[j] = false;
		}
		for (int i = 0; i < V; i++) {
			vMarked[v] = true;
			wMark[w] = true;
			for (int j = 0; j < V; j++) {
				if (adj[i][j] == 1 && vMarked[i]) {
					vCount++;
					verticesArray[vCount] = j;
					vMarked[j] = true;
				}
				if (adj[i][j] == 1 && wMark[i]) {
					wCount++;
					wArray[wCount] = j;
					wMark[j] = true;
				}
				if (wArray[wCount] == verticesArray[vCount]) {
					return wArray[wCount];
				}
			}
		}
		return -1;
	}
}
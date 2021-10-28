import static org.junit.Assert.*;

import org.junit.Test;

public class tests {
	@Test 
	public void testLCA(){
		LCA graph = new LCA(9);
		graph.addEdge(0, 1);   //7 and 8 are parent nodes, its kind of backwards
		graph.addEdge(0, 2);
		graph.addEdge(1, 3);
		graph.addEdge(2, 4);
		graph.addEdge(3, 5);
		graph.addEdge(4, 6);
		graph.addEdge(5, 7);
		graph.addEdge(6, 7);
		graph.addEdge(7, 8);
	    assertEquals("", 7, graph.LCAFind(3, 4));
		assertEquals("", 7, graph.LCAFind(1, 4));
		assertEquals("", 2, graph.LCAFind(2, 0));
	    assertEquals("", 7, graph.LCAFind(5, 2));
		assertEquals("", 5, graph.LCAFind(1, 5));
		assertEquals("", 7, graph.LCAFind(4, 3));
	    assertEquals("", 5, graph.LCAFind(5, 1));
		assertEquals("", 7, graph.LCAFind(5, 6));
		assertEquals("", 7, graph.LCAFind(3, 4));
		assertEquals("", 7, graph.LCAFind(2, 5));

	}

}
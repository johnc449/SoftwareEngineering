import static org.junit.Assert.*;

import org.junit.Test;

public class tests {
	@Test 
	public void testLCADAG(){
		LCA graph = new LCA(7);
		graph.addEdge(6, 3);   
		graph.addEdge(5, 2);
		graph.addEdge(3, 1);
		graph.addEdge(4, 1);
		graph.addEdge(4, 2);
		graph.addEdge(2, 0);
		graph.addEdge(1, 0);
		assertEquals("DAG Testing 1", 0, graph.LCAFind(5, 6));
	    assertEquals("DAG Testing 2", 1, graph.LCAFind(4, 3));
		assertEquals("DAG Testing 3", 0, graph.LCAFind(2, 0));
	    assertEquals("DAG Testing 4", 1, graph.LCAFind(4, 6));
		assertEquals("DAG Testing 5", 1, graph.LCAFind(3, 6));
		assertEquals("DAG Testing 6", 2, graph.LCAFind(4, 5));
	}
	@Test 
	public void testLCAOriginalTestsAdapted1(){
		LCA graph = new LCA(7);
		graph.addEdge(1, 0);  
		graph.addEdge(2, 0);
		graph.addEdge(3, 1);
		graph.addEdge(4, 1);
		graph.addEdge(5, 2);
		graph.addEdge(6, 2);
		assertEquals("Original Tests1", 1, graph.LCAFind(3, 4));
	    assertEquals("Original Tests2", 0, graph.LCAFind(3, 5));
		assertEquals("Original Tests3", 0, graph.LCAFind(2, 3));
	    assertEquals("Original Tests4", 0, graph.LCAFind(1, 3));
	    assertEquals("Original Tests5", 2, graph.LCAFind(6,5));
	}
	@Test 
	public void testLCAOriginalTestsAdapted2(){
		LCA graph = new LCA(7);
		graph.addEdge(1, 0);  
		graph.addEdge(2, 1);
		graph.addEdge(3, 2);
		graph.addEdge(4, 3);
		graph.addEdge(5, 4);
		graph.addEdge(6, 5);
		assertEquals("", 2, graph.LCAFind(3, 4));
		assertEquals("", 2, graph.LCAFind(4, 3));
	    assertEquals("", 4, graph.LCAFind(4, 4));
	}
	@Test 
	public void testLCAOriginalTestsAdapted3(){
		LCA graph = new LCA(2);
	    assertEquals("", -1, graph.LCAFind(4, 5));
	}

}
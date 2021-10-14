import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class tests {

    @Test
    public void LCATest(){
    	LCA tree = new LCA();
        tree.root = new Node(1);
        tree.root.left = new Node(2);
        tree.root.right = new Node(3);
        tree.root.left.left = new Node(4);
        tree.root.left.right = new Node(5);
        tree.root.right.left = new Node(6);
        tree.root.right.right = new Node(7);
 
        assertEquals("Test1", 2,tree.findLCA(4,5));
        assertEquals("Test2", 1,tree.findLCA(4,6));
        assertEquals("Test3", 1,tree.findLCA(3,4));
        assertEquals("Test4", 2,tree.findLCA(2,4));
        assertEquals("Test4", 3,tree.findLCA(7,6));
        
    }
    @Test
    public void LCATest1(){
    	LCA tree = new LCA();
        tree.root = new Node(1);
        tree.root.right = new Node(2);
        tree.root.right.right = new Node(3);
        tree.root.right.right.right = new Node(4);
        tree.root.right.right.right.right = new Node(5);
 
        assertEquals("Test1", 4,tree.findLCA(4,5));
        assertEquals("Test2", 2,tree.findLCA(2,5));
        assertEquals("Test3", 4,tree.findLCA(5,4));
        assertEquals("Test4", 5,tree.findLCA(5,5));
        
    }
    @Test
    public void LCATest2(){
    	LCA tree = new LCA();
        //tree.root = new Node(1);
 
        assertEquals("Test1", -1,tree.findLCA(4,5));
        
    }

}

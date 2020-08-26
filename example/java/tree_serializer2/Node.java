/**
 * Node class for representing a tree structure.
 *
 * Each node stores a value and a reference to it's left and right nodes.
 *
 * @param <T> The type of the value stored in a node.
 */
public class Node<T> {
    public T value;
    public Node<T> left;
    public Node<T> right;

    public Node(T value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }

    public Node(T value, Node<T> left, Node<T> right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }
}

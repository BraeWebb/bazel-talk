/**
 * Node class for representing a tree structure.
 *
 * Each node stores a value and a reference to it's left and right nodes.
 *
 * @param <T> The type of the value stored in a node.
 */
class Node<T> {
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

/**
 * Invalid format exception that is thrown when a
 * serialized node cannot be deserialized
 */
class InvalidFormat extends Exception {}

/**
 * A string processor for parsing through a string.
 *
 * Keeps a record of the character position within the string.
 */
class StringProcessor {
    private int position;
    private String reading;

    /**
     * Create a new string processor for the given string
     * starting at character position of zero.
     */
    public StringProcessor(String reading) {
        this.reading = reading;
        this.position = 0;
    }

    /**
     * Check that the next character is the given char.
     *
     * Throws an InvalidFormat exception if it is not.
     *
     * Advances the position reference along one character.
     */
    public void hasNext(char next) throws InvalidFormat {
        if (next() != next) {
            throw new InvalidFormat();
        }
    }

    /**
     * Get the next amount characters as a string.
     *
     * Advances the position reference along amount characters.
     */
    public String next(int amount) {
        position += amount;
        return reading.substring(position - amount, position);
    }

    /**
     * Get all the character up until the given character is found.
     *
     * Advances the position reference to one before the character being searched for.
     */
    public String nextTo(char character) {
        int offset = reading.indexOf(character, position) - position;
        return next(offset);
    }

    /**
     * Read the next character and advance the position reference by one.
     */
    public char next() {
        return reading.charAt(position++);
    }
}

public class SerializeTree {
    /**
     * Serialize a tree structure from it's root node.
     *
     * Creates a depth first nested representation of the structure.
     *
     * A node is serialised as ('value',left,right) where value is
     * the value stored within the node and left and right are the
     * serialization of the left and right subnodes (or null if no subnode exists).
     *
     * Example:
     * new Node<>("root", new Node<>("left", new Node<>("left.left"), null), new Node<>("right"))
     *
     * Serializes to
     *
     * ('root',('left',('left.left',null,null),null),('right',null,null))
     */
    public static <T> String serialize(Node<T> root) {
        if (root == null) {
            return "null";
        }

        StringBuilder builder = new StringBuilder();

        builder.append("('");
        builder.append(root.value);
        builder.append("',");

        builder.append(serialize(root.left));
        builder.append(",");
        builder.append(serialize(root.right));
        builder.append(")");

        return builder.toString();
    }

    /**
     * Helper method for deserializing a string.
     *
     * Passes the string processor recursively to keep track of the current position.
     */
    private static Node<String> deserialize(StringProcessor reader) throws InvalidFormat {
        // handle the null values sprinkled in
        char start = reader.next();
        if (start != '(') {
            if (start == 'n') {
                if (reader.next(3).equals("ull")) {
                    return null;
                }
            }
            throw new InvalidFormat();
        }

        // read the value of a node
        reader.hasNext('\'');
        String value = reader.nextTo('\'');
        reader.hasNext('\'');

        // read the left subnode
        reader.hasNext(',');
        Node<String> left = deserialize(reader);

        // read the right subnode
        reader.hasNext(',');
        Node<String> right = deserialize(reader);

        reader.hasNext(')');

        return new Node<>(value, left, right);
    }

    /**
     * Deserialize a tree structure from it's serialized string {@link SerializeTree#serialize(Node)}.
     *
     * Example:
     * ('root',('left',('left.left',null,null),null),('right',null,null))
     *
     * Deserializes to
     * new Node<>("root", new Node<>("left", new Node<>("left.left"), null), new Node<>("right"))
     */
    public static Node<String> deserialize(String node) throws InvalidFormat {
        return deserialize(new StringProcessor(node));
    }

    public static void main(String[] args) throws InvalidFormat {
        Node<String> node = new Node<>("root",
                new Node<>("left",
                        new Node<>("left.left"),
                        null),
                new Node<>("right"));

        System.out.println(serialize(node));
        System.out.println(serialize(deserialize(serialize(node))));

        assert deserialize(serialize(node)).left.left.value.equals("left.left");
    }
}
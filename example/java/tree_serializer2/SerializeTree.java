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
     * Deserialize a tree structure from it's serialized string {@link Daily3#serialize(Node)}.
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
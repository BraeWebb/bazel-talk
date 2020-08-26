/**
 * A string processor for parsing through a string.
 *
 * Keeps a record of the character position within the string.
 */
public class StringProcessor {
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
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Trie trie = new Trie();
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int m = input.nextInt();

        String[] autocompletes = new String[n];
        String[] searches = new String[m];
        input.nextLine();
        for (int i = 0; i < n; i++) {
            autocompletes[i] = input.nextLine();
        }

        input.nextLine();

        for (int i = 0; i < m; i++) {
            searches[i] = input.nextLine();
        }
        for (String word : autocompletes) {
            trie.insert(word);
        }

        for (String word : searches) {
            System.out.println(trie.prefixesFoundUpTo(word));
        }
                
    }

}

class TrieNode {
    public TrieNode[] children = new TrieNode[128];
    public int count = 0;
    
    public TrieNode() {
    }
}

class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    public void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            if (node.children[c - 'A'] == null) {
                node.children[c - 'A'] = new TrieNode();
            }
            node = node.children[c - 'A'];
            node.count += 1;
        }
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    public int prefixesFoundUpTo(String prefix) {
        TrieNode node = root;
        int ret = 0;
        for (char c : prefix.toCharArray()) {
            if (node.children[c - 'A'] == null) 
            return ret;
            node = node.children[c - 'A'];
            ret += node.count;
        }
        return ret;
    }
}
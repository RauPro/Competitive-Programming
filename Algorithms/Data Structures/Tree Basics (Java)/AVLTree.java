import java.util.NoSuchElementException;

// Every vertex in this BST is a Java Class
class BSTVertex {
    BSTVertex(int v) {
        key = v;
        parent = left = right = null;
        height = 0;
    }

    // all these attributes remain public to slightly simplify the code
    public BSTVertex parent, left, right;
    public int key;
    public int height; // will be used in AVL lecture
}

// This is just a sample implementation
// There are other ways to implement BST concepts...
class BST {
    protected BSTVertex root;

    protected BSTVertex search(BSTVertex T, int v) {
        if (T == null) return T;                                  // not found
        else if (T.key == v) return T;                                      // found
        else if (T.key < v) return search(T.right, v);       // search to the right
        else return search(T.left, v);         // search to the left
    }

    protected BSTVertex insert(BSTVertex T, int v) {
        if (T == null) return new BSTVertex(v);          // insertion point is found

        if (T.key < v) {                                      // search to the right
            T.right = insert(T.right, v);
            T.right.parent = T;
        } else {                                                 // search to the left
            T.left = insert(T.left, v);
            T.left.parent = T;
        }

        return T;                                          // return the updated BST
    }

    protected void inorder(BSTVertex T) {
        if (T == null) return;
        inorder(T.left);                               // recursively go to the left
        System.out.printf(" %d", T.key);                      // visit this BST node
        inorder(T.right);                             // recursively go to the right
    }

    // Example of Java error handling mechanism
  /* // old code, returns -1 when there is no minimum (the BST is empty)
  protected int findMin(BSTVertex T) {
         if (T == null)      return -1;                             // not found
    else if (T.left == null) return T.key;                    // this is the min
    else                     return findMin(T.left);           // go to the left
  }
  */

    protected int findMin(BSTVertex T) {
        if (T == null) throw new NoSuchElementException("BST is empty, no minimum");
        else if (T.left == null) return T.key;                    // this is the min
        else return findMin(T.left);           // go to the left
    }

    protected int findMax(BSTVertex T) {
        if (T == null) throw new NoSuchElementException("BST is empty, no maximum");
        else if (T.right == null) return T.key;                   // this is the max
        else return findMax(T.right);        // go to the right
    }

    protected int successor(BSTVertex T) {
        if (T.right != null)                       // this subtree has right subtree
            return findMin(T.right);  // the successor is the minimum of right subtree
        else {
            BSTVertex par = T.parent;
            BSTVertex cur = T;
            // if par(ent) is not root and cur(rent) is its right children
            while ((par != null) && (cur == par.right)) {
                cur = par;                                         // continue moving up
                par = cur.parent;
            }
            return par == null ? -1 : par.key;           // this is the successor of T
        }
    }

    protected int predecessor(BSTVertex T) {
        if (T.left != null)                         // this subtree has left subtree
            return findMax(T.left);  // the predecessor is the maximum of left subtree
        else {
            BSTVertex par = T.parent;
            BSTVertex cur = T;
            // if par(ent) is not root and cur(rent) is its left children
            while ((par != null) && (cur == par.left)) {
                cur = par;                                         // continue moving up
                par = cur.parent;
            }
            return par == null ? -1 : par.key;           // this is the successor of T
        }
    }

    protected BSTVertex delete(BSTVertex T, int v) {
        if (T == null) return T;              // cannot find the item to be deleted

        if (T.key == v) {                          // this is the node to be deleted
            if (T.left == null && T.right == null)                   // this is a leaf
                T = null;                                      // simply erase this node
            else if (T.left == null && T.right != null) {   // only one child at right
                T.right.parent = T.parent;             // ma, take care of my only child
                T = T.right;                                                 // bypass T
            } else if (T.left != null && T.right == null) {    // only one child at left
                T.left.parent = T.parent;              // ma, take care of my only child
                T = T.left;                                                  // bypass T
            } else {                // has two children, find successor to avoid quarrel
                int successorV = successor(v);             // predecessor is also OK btw
                T.key = successorV;         // replace this key with the successor's key
                T.right = delete(T.right, successorV);      // delete the old successorV
            }
        } else if (T.key < v)                                   // search to the right
            T.right = delete(T.right, v);
        else                                                   // search to the left
            T.left = delete(T.left, v);
        return T;                                          // return the updated BST
    }

    public BST() {
        root = null;
    }

    public int search(int v) {
        BSTVertex res = search(root, v);
        return res == null ? -1 : res.key;
    }

    public void insert(int v) {
        root = insert(root, v);
    }

    public void inorder() {
        inorder(root);
        System.out.println();
    }

    public int findMin() {
        return findMin(root);
    }

    public int findMax() {
        return findMax(root);
    }

    public int successor(int v) {
        BSTVertex vPos = search(root, v);
        return vPos == null ? -1 : successor(vPos);
    }

    public int predecessor(int v) {
        BSTVertex vPos = search(root, v);
        return vPos == null ? -1 : predecessor(vPos);
    }

    public void delete(int v) {
        root = delete(root, v);
    }

    // will be used in AVL lecture
    protected int getHeight(BSTVertex T) {
        if (T == null) return -1;
        else return Math.max(getHeight(T.left), getHeight(T.right)) + 1;
    }

    public int getHeight() {
        return getHeight(root);
    }
}

public class AVLTree extends BST {
    public AVLTree() {
        root = null;
    }

    private int h(BSTVertex T) {
        return T == null ? -1 : T.height;
    }

    protected BSTVertex rotateLeft(BSTVertex T) {
        // T must have a right child

        BSTVertex w = T.right;
        w.parent = T.parent;
        T.parent = w;
        T.right = w.left;
        if (w.left != null) w.left.parent = T;
        w.left = T;

        T.height = Math.max(h(T.left), h(T.right)) + 1;
        w.height = Math.max(h(w.left), h(w.right)) + 1;

        return w;
    }

    protected BSTVertex rotateRight(BSTVertex T) {
        // T must have a left child

        BSTVertex w = T.left;
        w.parent = T.parent;
        T.parent = w;
        T.left = w.right;
        if (w.right != null) w.right.parent = T;
        w.right = T;

        T.height = Math.max(h(T.left), h(T.right)) + 1;
        w.height = Math.max(h(w.left), h(w.right)) + 1;

        return w;
    }

    protected BSTVertex insert(BSTVertex T, int v) {
        if (T == null) return new BSTVertex(v);          // insertion point is found

        if (T.key < v) {                                      // search to the right
            T.right = insert(T.right, v);
            T.right.parent = T;
        } else {                                                 // search to the left
            T.left = insert(T.left, v);
            T.left.parent = T;
        }

        int balance = h(T.left) - h(T.right);
        if (balance == 2) { // left heavy
            int balance2 = h(T.left.left) - h(T.left.right);
            if (balance2 == 1) {
                T = rotateRight(T);
            } else { // -1
                T.left = rotateLeft(T.left);
                T = rotateRight(T);
            }
        } else if (balance == -2) { // right heavy
            int balance2 = h(T.right.left) - h(T.right.right);
            if (balance2 == -1)
                T = rotateLeft(T);
            else { // 1
                T.right = rotateRight(T.right);
                T = rotateLeft(T);
            }
        }

        T.height = Math.max(h(T.left), h(T.right)) + 1;
        return T;                                          // return the updated AVL
    }

    protected BSTVertex delete(BSTVertex T, int v) {
        if (T == null) return T;              // cannot find the item to be deleted

        if (T.key == v) {                          // this is the node to be deleted
            if (T.left == null && T.right == null)                   // this is a leaf
                T = null;                                      // simply erase this node
            else if (T.left == null && T.right != null) {   // only one child at right
                BSTVertex temp = T;
                T.right.parent = T.parent;
                T = T.right;                                                 // bypass T
                temp = null;
            } else if (T.left != null && T.right == null) {    // only one child at left
                BSTVertex temp = T;
                T.left.parent = T.parent;
                T = T.left;                                                  // bypass T
                temp = null;
            } else {                                 // has two children, find successor
                int successorV = successor(v);
                T.key = successorV;         // replace this key with the successor's key
                T.right = delete(T.right, successorV);      // delete the old successorV
            }
        } else if (T.key < v)                                   // search to the right
            T.right = delete(T.right, v);
        else                                                   // search to the left
            T.left = delete(T.left, v);

        if (T != null) {               // similar as insertion code except this line
            int balance = h(T.left) - h(T.right);
            if (balance == 2) { // left heavy
                int balance2 = h(T.left.left) - h(T.left.right);
                if (balance2 == 1) {
                    T = rotateRight(T);
                } else { // -1
                    T.left = rotateLeft(T.left);
                    T = rotateRight(T);
                }
            } else if (balance == -2) { // right heavy
                int balance2 = h(T.right.left) - h(T.right.right);
                if (balance2 == -1)
                    T = rotateLeft(T);
                else { // 1
                    T.right = rotateRight(T.right);
                    T = rotateLeft(T);
                }
            }

            T.height = Math.max(h(T.left), h(T.right)) + 1;
        }

        return T;                                          // return the updated BST
    }
}

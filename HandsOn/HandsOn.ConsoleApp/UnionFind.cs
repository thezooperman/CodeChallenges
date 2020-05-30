using System;
using System.Linq;

namespace HandsOn.ConsoleApp
{
    public class UnionFind
    {
        private int _size;
        private int[] _setSize;
        private int[] _id;
        private int _totalSet;

        public UnionFind(int size)
        {
            if (size <= 0)
                throw new ArgumentException("Size must be > 0");

            this._size = size;
            this._totalSet = size;
            this._setSize = new int[size];
            this._id = new int[size];

            foreach (int i in Enumerable.Range(0, size))
            {
                this._setSize[i] = 1;
                this._id[i] = i;
            }
        }

        public int find(int p)
        {
            int root = p;

            // Find which set the item belong to
            // parent of the item
            while (root != this._id[root])
            {
                root = this._id[root];
            }

            // compress the set on its path to root
            while (p != root)
            {
                int next = this._id[p];
                this._id[p] = root;
                p = next;
            }

            return root;
        }

        public bool isConnected(int p, int q)
        {
            return this.find(p) == this.find(q);
        }

        public int getSetSize(int p)
        {
            return this._setSize[this.find(p)];
        }

        public int getTotalSet()
        {
            return this._totalSet;
        }

        public void union(int p, int q)
        {
            // both items are in same set
            if (this.isConnected(p, q))
                return;

            int root1 = this.find(p);
            int root2 = this.find(q);

            // merge smaller set into larger
            if (this._setSize[root1] <= this._setSize[root2])
            {
                this._setSize[root2] += this._setSize[root1];
                // make root2 parent of root1
                this._id[root1] = root2;
            }
            else
            {
                this._setSize[root1] += this._setSize[root2];
                this._id[root2] = root1;
            }

            this._totalSet--;
        }
    }
}


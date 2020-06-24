using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using System.Linq;

namespace HandsOn.ConsoleApp
{
    public class Kruskals
    {
        class Edge : IComparable<Edge>
        {
            private int _source, _destination, _weight;
            public int Source
            {
                get => this._source;
                set => this._source = value;
            }
            public int Destination
            {
                get => this._destination;
                set => this._destination = value;
            }
            public int Weight
            {
                get => this._weight;
                set => this._weight = value;
            }

            public int CompareTo([AllowNull] Edge other)
            {
                return this._weight - other.Weight;
            }
        }

        class Graph
        {
            private int _verticesCount;
            public int VerticesCount
            {
                get => this._verticesCount;
                set => this._verticesCount = value;
            }

            private int _edgesCount;
            public int EdgesCount
            {
                get => this._edgesCount;
                set => this._edgesCount = value;
            }

            private IList<Edge> _edges;
            public IList<Edge> Edges
            {
                get => this._edges;
                set => this._edges = value;
            }
        }

        class UnionFind
        {
            private int _size, _totalSets;
            private int[] _setSize, _id;

            public UnionFind(int size)
            {
                this._size = size;
                this._totalSets = size;
                this._setSize = new int[size];
                this._id = new int[size];

                // Initialize Set and Id
                Enumerable.Range(0, size).ToList().ForEach(i =>
                {
                    this._setSize[i] = 1;
                    this._id[i] = i;
                });
            }

            public int Find(int vertex)
            {
                int root = vertex;

                while (root != this._id[root])
                {
                    root = this._id[root];
                }

                while (vertex != root)
                {
                    int next = this._id[vertex];
                    this._id[vertex] = root;
                    vertex = next;
                }

                return root;
            }

            public void Union(int p, int q)
            {
                if (this.Find(p) == this.Find(q))
                    return;

                int p_root = this.Find(p);
                int q_root = this.Find(q);

                if (this._setSize[p_root] < this._setSize[q_root])
                {
                    this._setSize[q_root] += this._setSize[p_root];
                    this._id[p_root] = q_root;
                }
                else
                {
                    this._setSize[p_root] += this._setSize[q_root];
                    this._id[q_root] = p_root;
                }

                this._totalSets--;
            }
        }

        Graph CreateGraph(int vertices, int edges)
        {
            Graph graph = new Graph();

            var edgeList = new List<Edge>{
             new Edge{Source = 0,  Destination = 1, Weight= 10},
             new Edge{Source = 0,  Destination = 2, Weight= 6},
             new Edge{Source = 0,  Destination = 3, Weight= 5},
             new Edge{Source = 1,  Destination = 3, Weight= 15},
             new Edge{Source = 2,  Destination = 3, Weight= 4}
            };
            graph.EdgesCount = edges;
            graph.VerticesCount = vertices;
            graph.Edges = new List<Edge>(edges);

            for (int i = 0; i < edgeList.Count; i++)
               graph.Edges.Add(edgeList[i]);

            return graph;
        }

        void MST(Graph graph)
        {
            var vertices = graph.VerticesCount;
            var edges = graph.EdgesCount;
            IList<Edge> result = new List<Edge>(vertices);

            // sort the graph by weight
            graph.Edges.ToList().Sort();

            var uf = new UnionFind(graph.Edges.Count);
            int i , e;
            i = e = 0;
            while (e < vertices)
            {
                Edge next = graph.Edges[i++];
                int x = uf.Find(next.Source);
                int y = uf.Find(next.Destination);

                if (x != y){
                    result[e++] = next;
                    uf.Union(x, y);
                }
            }

            this.Show(result);
        }

        void Show(IList<Edge> result){
            foreach (Edge edge in result)
                System.Console.WriteLine("{0} -- {1} == {2}", edge.Source, edge.Destination, edge.Weight);
        }

        public void FindMST(int v, int e){
            var graph = this.CreateGraph(v, e);
            this.MST(graph);
        }
    }
}
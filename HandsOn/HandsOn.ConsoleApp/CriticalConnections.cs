using System;
using System.Collections.Generic;

namespace HandsOn.ConsoleApp
{
    public class CriticalConnections
    {

        #region Tarjan's Algorithm
        internal struct Vertex{
            private int _id;
            public int Id
            {
                get { return _id; }
                set { _id = value; }
            }
            
            private int _index;
            public int Index
            {
                get { return _index; }
                set { _index = value; }
            }

           private int _lowLink;
           public int LowLink
           {
               get { return _lowLink; }
               set { _lowLink = value; }
           }

           public HashSet<Vertex> Dependencies {get;set;}
        }
        #endregion

        #region NonTarjanDFS
        private IDictionary<int, IList<int>> graph;

        private void BuildGraph(int n, IList<IList<int>> edges)
        {
            this.graph = new Dictionary<int, IList<int>>();

            for (int i = 1; i <= n; i++)
                this.graph[i] = new List<int>();

            foreach (var edge in edges)
            {
                this.graph[edge[0]].Add(edge[1]);
                this.graph[edge[1]].Add(edge[0]);
            }
        }

        private void dfs(IDictionary<int, IList<int>> subGraph, int source, HashSet<int> visited)
        {
            if (visited.Contains(source))
                return;

            visited.Add(source);
            foreach (var node in subGraph[source])
                this.dfs(subGraph, node, visited);
        }

        public IList<IList<int>> GetCriticalConnections(int n, IList<IList<int>> connections)
        {
            this.BuildGraph(n, connections);

            IList<IList<int>> final = new List<IList<int>>();

            foreach (IList<int> connection in connections)
            {
                int from, to;
                from = connection[0];
                to = connection[1];

                if (graph.ContainsKey(from)){
                    graph[from].Remove(to);
                    graph[to].Remove(from);

                    var visited = new HashSet<int>();

                    this.dfs(graph, from, visited);

                    if (visited.Count != n)
                        final.Add(new List<int>(connection));
                    
                    // add the edge back
                    graph[from].Add(to);
                    graph[to].Add(from);
                }
            }

            System.Console.Write("Critical Nodes...");
            foreach (var item in final)
                System.Console.WriteLine("{0},{1}", item[0], item[1]);

            return final;
        }

        #endregion
    }
}
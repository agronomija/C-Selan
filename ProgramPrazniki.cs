using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Prazniki
{
	class Program
	{
		static void Main(string[] args)
		{
		    void EasterMonday(int year)
			{
				int A = year % 19;
				Console.WriteLine(A);
				int B = year / 100;
				Console.WriteLine(B);
				int C = year % 100;
				Console.WriteLine(C);
				int D = (B / 4);
				Console.WriteLine(D);
				int E = (B % 4);
				Console.WriteLine(E);
				int G = (8 * B + 13) / 25;
				Console.WriteLine(G);
				int H = (19 * A + B - D - G + 15) % 30;
				Console.WriteLine(H);
				int M = (A + 11 * H) / 319;
				Console.WriteLine(M);
				int J = C / 4;
				Console.WriteLine(J);
				int K = C % 4;
				Console.WriteLine(K);
				int L = (2 * E + 2 * J - K - H + M + 32) % 7;
				Console.WriteLine(L);
				int N = (H - M + L + 90) / 25;
				Console.WriteLine(N);
				int P = (H - M + L + N + 19) % 32;
				Console.WriteLine(P);
				var datum = new DateTime(year, N, P);
				Console.WriteLine(datum.ToLongDateString());
				Console.WriteLine(datum.ToShortDateString());

				Console.ReadKey();

			}



			Dictionary<int, string> d = new Dictionary<int, string>();
			d.Add(1, 'Hello');
			d.Add(2, 'World');

			Console.WriteLine(d);
			Console.ReadKey();
				
		}
	}
}

#include <iostream>
#include <string>
#include <bitset>
#include <set>
#include <vector>

using namespace std;
#define PRIME_MAX 1000000
#define ASUM_MAX 28123

/* Non-abundant sums
 * 
 * A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
 * For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
 * which means that 28 is a perfect number.
 *
 * A number n is called deficient if the sum of its proper divisors is less than n and
 * it is called abundant if this sum exceeds n.
 *
 * As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can 
 * be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown
 * that all integers greater than 28123 can be written as the sum of two abundant numbers. However,
 * this upper limit cannot be reduced any further by analysis even though it is known that the
 * greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
 *
 * Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
 *
 */

class PrimeGenerator
{
	private:
		bitset<PRIME_MAX> sieve;
		int limit;
		set<int> primes;

		void generate() {
			for(int i = 2; i <= limit; i++) { 
				for(int j = 2; j <= limit; j++) {
					if (i*j >= limit) break;
					sieve.reset(i*j);
				}
			}

			sieve.set(2);

			for(int i = 0; i < limit; i++)
				if (sieve[i]) primes.insert(i);
		}

	public:
		PrimeGenerator(int n = 30) {
			sieve.set();
			sieve.reset(0);
			sieve.reset(1);
			limit = n+1;
			if (limit > sieve.size()) abort();
			generate();
		}

		set<int> get_primes() {
			return primes;
		}
		

		set<int> get_prime_factors(int n) {
			auto results = set<int>();
			if (n > limit) abort();
			results.insert(1);

			for(int p : primes) {
				int test = 0;
				while (test < n) {
					test += p;
					if (test == n) continue;
					if (n % test == 0) 
						results.insert(test);
				}
			}
			return results;
		}
};

int main()
{
	int cnt = 0;
	auto a_sum = set<int>();
	auto v = vector<int>();
	auto bs = bitset<ASUM_MAX+1>();
	int fsum = 0;

	bs.set();
	for (int n = 1; n <= ASUM_MAX; n++)
	{ 
		auto p = PrimeGenerator(n);
		int sum = 0;
		for (int j : p.get_prime_factors(n))
			sum += j;

		if (sum > n) {
			a_sum.insert(n);
			v.push_back(n);
		}

	}

	for (int j = 0 ; j <= ASUM_MAX; j++) {
		/* search for nearest abundant sum */
		for (int k = 0; k < v.size() && j > v[k]; k++) {
			int diff = j - v[k];
			if (a_sum.count(diff)) {
				bs.reset(j);
				break;
			}
		}
	}

	for (int i = 0; i < bs.size(); i++) {
		if (bs[i]) {
			fsum += i;
		}
	}

	cout << "sum " << fsum << "\n";

	return 0;
}

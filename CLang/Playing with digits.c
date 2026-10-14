int digPow(int n, int p) {
  int rem = 0, total = 0, temp_total = 1;
  int temp_p = p, temp_n = n;
  
  while (n != 0) // count digits, store in p.
    {
      rem = n%10;
      p = p + 1;
      n = n/10;
    }
  
  p = p - 1; // since we have to take in the first value of p as well.
  n = temp_n;
  temp_p = p;
  
  while (n != 0)
    {
      rem = n%10;
      
      while (temp_p != 0)
        {
          temp_total = temp_total * rem;
          temp_p = temp_p - 1;
        }
      
      p = p - 1;
      total = total + temp_total;
      temp_total = 1;
      temp_p = p;
      n = n/10;
    }

void main()
{
  int result = digPow(89, 1);
}

/*

Playing with digits

Some numbers have funny properties. For example:

89 --> 8¹ + 9² = 89 * 1
695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Note: n and p will always be strictly positive integers.

Examples:
n = 89; p = 1 ---> 1 since 8¹ + 9² = 89 = 89 * 1

n = 92; p = 1 ---> -1 since there is no k such that 9¹ + 2² equals 92 * k

n = 695; p = 2 ---> 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2

n = 46288; p = 3 ---> 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

*/

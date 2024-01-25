#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define e "\n"
void solve()
{
    int n, c = 0;
    cin >> n;
    string scontainer, maincontainer;
    cin >> scontainer >> maincontainer;
    for (int i = 0; i < n; i++)
    {
        if (scontainer[i] == '0' && maincontainer[i] == '1')
        {
            scontainer[i] = '1';
            c++;
        }
        else if (scontainer[i] == '1' && maincontainer[i] == '1')
        {
            scontainer[i] = '0';
            c++;
        }
    }
    cout << c << e;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t = 1;
    cin >> t;

    while (t--)
    {
        solve();
    }

    return 0;
}
/*
1 2
4 5
1 5
4 2
*/
#include<iostream>
#include<random>
#include<fstream>
#include<cstdlib>
#include<time.h>

int main( )
{
    srand(time(NULL));
    
    const int kroki = 1000;
    const int N = 100;
    int krok_set = 1;
    int pozycja[N] = {};
    int krok;

    std::ofstream f, f2;
    std::string name, name2;
    name = "spacer3.txt"; //do gnuplota
    name2 = "spacer3-py-stat.txt";
    f.open(name); //gnuplot
    f2.open(name2); 

    for (int i = 0; i < kroki; i++) //petla na kroki
    {
        f << i << " ";

        for (int j = 0; j < N; j++) //petla po spacerach wszystkich
        {
            krok = rand( ) % 2 ? krok_set : -krok_set;
            pozycja[j] += krok;

            f << pozycja[j] << " ";
            f2 << pozycja[j] << " ";
        }
        
        f << "\n";
        f2 << "\n";
    }

    f.close( );
}
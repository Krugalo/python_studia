#include<iostream>
#include<random>
#include<fstream>
#include<cstdlib>
#include<time.h>

int main( )
{
    srand(time(NULL));

    const int N = 100; //liczba krokow
    int krok;
    int krok_set = 1;
    int pozycja = 0;
    int pozycja2d[2] = {};

    std::ofstream f1d, f2d;
    std::string name1d, name2d;
    name1d = "spacer2-1d.txt";
    name2d = "spacer2-2d.txt";
    

    int d;
    
    std::cout << "Podaj ile d spacer chcesz zasymulowac: ";
    std::cin >> d; //1 albo 2

    switch (d)
    {
    case 1:
        f1d.open(name1d);
        for (int i = 0; i < N; i++)
        {
            krok = rand( ) % 2 ? krok_set : -krok_set;
            pozycja += krok;

            std::cout << pozycja << '\n';
            std::cout << krok << '\n';
            f1d << i << " " << pozycja << '\n';
        }
        f1d.close( );
        break;
    case 2:
        f2d.open(name2d);
        for (int i = 0; i < N; i++)
        {
            krok = rand( ) % 4;
            
            if (krok == 0)
            {
                pozycja2d[0] += krok_set;
            }
            else if (krok == 1)
            {
                pozycja2d[0] -= krok_set;
            }
            else if (krok == 2)
            {
                pozycja2d[1] += krok_set;
            }
            else if (krok == 3)
            {
                pozycja2d[1] -= krok_set;
            }

            for (int i = 0; i < 2; i++)
            {
                std::cout << pozycja2d[i] << " ";
            }
            std::cout << '\n';
            f2d << i << " " << pozycja2d[0] << " " << pozycja2d[1] << '\n';
        }
        f2d.close( );
        break;
    default:
        std::cout << "tylko 1 lub 2!!!" << '\n';
        break;
    }

    return 0;
}
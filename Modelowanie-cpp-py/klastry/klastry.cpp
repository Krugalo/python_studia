#include<iostream>
#include<random>
#include<cstdlib>
#include<fstream>
#include<time.h>
#include<vector>

struct komorka
{
    //czy zyje
    bool x = 0;

    //lokacja
    int i;
    int j;
};


int main( )
{
    //rozmiar
    const int N = 100;

    //iteracje
    int counter = 1000;

    //rand
    srand(time(NULL));
    int temp;

    //kluster
    komorka klust[N][N];
    std::vector< komorka > sasiedzi;

    //komorki pamietaja gdzie sa
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            klust[i][j].i = i;
            klust[i][j].j = j;
        }
    }

    
    //center n/2
    klust[N / 2][N / 2].x = 1;


    //std::cout << "test 1" << '\n';

    //symulacja
    for (int z = 0; z < counter; z++)
    {
        //std::cout << z << '\n';
        sasiedzi.clear( );
        //zliczenie komórek
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (klust[i][j].x == 1)
                {
                    if (klust[i - 1][j].x == 0)
                    {
                        sasiedzi.push_back(klust[i - 1][j]);
                    }
                    if (klust[i + 1][j].x == 0)
                    {
                        sasiedzi.push_back(klust[i + 1][j]);
                    }
                    if (klust[i][j - 1].x == 0)
                    {
                        sasiedzi.push_back(klust[i][j - 1]);
                    }
                    if (klust[i][j + 1].x == 0)
                    {
                        sasiedzi.push_back(klust[i][j + 1]);
                    }

                }               
            }
        }

        temp = rand( ) % sasiedzi.size( );
        klust[sasiedzi[temp].i][sasiedzi[temp].j].x = 1;
    }

    //promien

    int licznik = 0;
    int counti1 = 0; //-
    int counti2 = 0; //+
    int countj1 = 0; //-
    int countj2 = 0; //+
    int ilei1, ilei2, ilej1, ilej2;
    int tempi, tempj;
    
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (klust[i][j].x == 1)
            {
                licznik++;
                tempi = i - N / 2;
                tempj = j - N / 2;

                //srodek masy
                if (tempi < 0)
                {
                    counti1 += tempi;
                }
                else
                {
                    counti2 += tempi;
                }
                if (tempj < 0)
                {
                    countj1 += tempj;
                }
                else
                {
                    countj2 += tempj;
                }
            }
            //std::cout << licznik << " " << counti1 << " " << counti2 << " " << countj1 << " " << countj2 << '\n';
        }
    }
    int Px, Py, Rx, Ry, R, c;

    c = (std::abs(counti1) < std::abs(counti2)) ? counti2 : counti1;
    Px = c / licznik;
    c = (std::abs(countj1) < std::abs(countj2)) ? countj2 : countj1;
    Py = c / licznik;
    std::cout << "Px = " << Px << ", Py = " << Py << '\n';

    //zliczanie x:
    int i = Px;
    do
    {
        ilei1++;
        i++;
    }
    while (klust[i + N/2][Py + N/2].x == 1);

    i = Px;
    do
    {
        ilei2++;
        i--;
    }
    while (klust[i + N/2][Py + N/2].x == 1);

    i = Py;
    do
    {
        ilej1++;
        i++;
    }
    while (klust[Px + N/2][i + N/2].x == 1);

    i = Py;
    do
    {
        ilej2++;
        i--;
    }
    while (klust[Py + N/2][i + N/2].x == 1);

    

    Rx = Py + std::max(ilei1, ilei2);
    Ry = Py + std::max(ilej1, ilej2);
    std::cout << "Rx = " << Rx << ", Ry = " << Ry << '\n';
    
    R = std::max(Ry, Rx);
    std::cout << "R = " << R << '\n';

    //std::cout << "test 2" << '\n';


    //plik
    std::ofstream f;
    std::string name;
    name = "kluster.txt";
    f.open(name);

    std::string tekst;
    
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (klust[i][j].x == 1)
            {
                tekst = "*";
            } else
            {
                tekst = " ";
            }
            
            
            f << tekst << " ";
        }
        f << '\n';
        //std::cout << '\n';
    }
    
    f.close( );

    //std::cout << "test 3" << '\n';
}
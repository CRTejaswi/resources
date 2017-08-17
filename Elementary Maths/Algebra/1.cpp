/* C++: Add two (m x n) matrices */
#include <iostream>
#include <conio.h>
#define n 5
using namespace std;

/* Function Declarations */
void inputMatrix (int MatX[][n],int m, int n0);
void outputMatrix (int MatX[][n],int m, int n0);
void addMatrix (int A[][n],int B[][n],int C[][n],int m, int n0);

main(){
    /* Input Matrix Dimensions */
    int m,n0;
    cout<<"Enter No. of (Rows,Columns) in Matrix: ";
    cin>>m>>n0;
    /* Initialize Matrices */
    int MatA[m][n],MatB[m][n],MatC[m][n];
    /* Input Matrix Elements */
    cout<<"############### Matrix A ###############"<<endl;
    inputMatrix(MatA,m,n0);
    cout<<"############### Matrix B ###############"<<endl;
    inputMatrix(MatB,m,n0);
    /* Compute & Display Result */
    addMatrix(MatA,MatB,MatC,m,n0);
    cout<<"########################################"<<endl;
    outputMatrix(MatC,m,n0);
    getch();
}
/* Function Definitions */
void inputMatrix (int MatX[][n],int m, int n0){
        for (int i = 0; i<m; i++)
            for (int j = 0; j<n0; j++){
                cout<<"Element["<<i<<","<<j<<"] Value: ";
                cin>>MatX[i][j];
            }
}
void outputMatrix (int MatX[][n],int m, int n0){
    cout<<"########### Resultant Matrix ###########"<<endl;
    for (int i = 0; i<m; i++){
        for (int j = 0; j<n0; j++)
            cout<<"X["<<i<<","<<j<<"] = "<<MatX[i][j]<<'\t';
        cout<<endl;
    }
}
void addMatrix (int A[][n],int B[][n],int C[][n],int m, int n0){
    for (int i = 0; i<n; i++)
        for (int j = 0; j<n; j++)
                C[i][j] = A[i][j] + B[i][j] ;
}
/*
Note:
 1. Here, matrices A,B,C are 'm x n', but evaluations are made for 'm x n0'.
     int MatA[m][n],MatB[m][n],MatC[m][n];
    where user chooses dimensions of matrices (m x n0) to work upon.
    This is because we have to initialize a matrix as A[][n] atleast. So we need atleast one parameter to be fixed for the compiler to allocate space.
 2. Also, no Array values are returned explicitly.
     void inputMatrix (...)
     void outputMatrix (...)
     void addMatrix (...)
*/`
#include <iostream>

#define LINUXOCCI //         

#include <occi.h>

using namespace std;

using namespace oracle::occi;

int main()
{

   Environment *env=Environment::createEnvironment(Environment::DEFAULT);

   cout<<"success"<<endl;

   string name = "c##sqlDB";

   string pass = "1234";

   string srvName = "1521/ex";

   try

   {

      Connection *conn = env->createConnection(name, pass);

      cout<<"conn success"<<endl;

      env->terminateConnection(conn);

   }

   catch(SQLException e)

   {

      cout<<e.what()<<endl;

       return -1;

   }

   Environment::terminateEnvironment(env);

   cout<<"end!"<<endl;

   return 0;
}
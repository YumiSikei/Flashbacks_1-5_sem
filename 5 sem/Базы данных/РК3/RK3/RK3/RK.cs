using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.Data.SqlClient;
using System.Data.Linq;
using System.Data.Linq.Mapping;
using System.Reflection;

namespace RK
{
    class C_RK
    {
        private static string connectionString = @"Data Source=.\SQLEXPRESS;Initial Catalog= TEST; Integrated Security=True";
       
        
        public void Linq1()
        {
            DataContext db = new DataContext(connectionString);

            var driver = from v in db.GetTable<Bus>() join m in db.GetTable<Way>()  on v.ID equals m.Bus where m.Num == 157 select v.BusDriver;

            foreach (var d in driver)
                Console.WriteLine(d);
            Console.WriteLine();
        }

        public void ADO1()
        {
            const string queryString = @"SELECT BusDriver FROM RK.Bus JOIN RK.WAY ON RK.Bus.ID = RK.WAY.Bus WHERE RK.Way.Num = 157";

            SqlConnection connection = new SqlConnection(connectionString);
            connection.Open();

            SqlCommand command = new SqlCommand(queryString, connection);

            SqlDataReader dataReader = command.ExecuteReader();
            while (dataReader.Read())
                Console.WriteLine(dataReader[0].ToString());

            dataReader.Close();
            connection.Close();
        }

       
        public void Linq2()
        {
            DataContext db = new DataContext(connectionString);

            var BID = from m in db.GetTable<Way>() group m by m.Num into j select new { Count = j.Count()};

            foreach (var d in BID)
                Console.WriteLine(d);
            Console.WriteLine();

        }
       
        public void ADO2()
        {
            const string queryString = @"SELECT RK.Way.Num FROM RK.Bus JOIN RK.WAY ON RK.Bus.ID = RK.WAY.Bus WHERE (SELECT Count(*) FROM RK.Bus JOIN RK.WAY ON RK.Bus.ID = RK.WAY.Bus) >= 10";

            SqlConnection connection = new SqlConnection(connectionString);
            connection.Open();

            SqlCommand command = new SqlCommand(queryString, connection);

            SqlDataReader dataReader = command.ExecuteReader();
            while (dataReader.Read())
                Console.WriteLine(dataReader[0].ToString());

            dataReader.Close();
            connection.Close();
        }

       
        
        public void Linq3()
        {

            DataContext db = new DataContext(connectionString);

            var list = (from v in db.GetTable<Bus>() join m in db.GetTable<Way>() on v.ID equals m.Bus where m.Num == 157 select v.Mark).Take(3);

            foreach (var d in list)
                Console.WriteLine(d);
            Console.WriteLine();

        }
        
        public void ADO3()
        {
            const string queryString = @"SELECT TOP(3) Mark  FROM RK.Bus JOIN RK.WAY ON RK.Bus.ID = RK.WAY.Bus WHERE RK.Way.Num = 157";
            
            SqlConnection connection = new SqlConnection(connectionString);
            connection.Open();

            SqlCommand command = new SqlCommand(queryString, connection);

            SqlDataReader dataReader = command.ExecuteReader();
            while (dataReader.Read())
                Console.WriteLine(dataReader[0].ToString());

            dataReader.Close();
            connection.Close();
        }

        public C_RK() {
            Linq1();
            Linq2();
            Linq3();
            ADO1();
            ADO2();
            ADO3();
        }
    }
}

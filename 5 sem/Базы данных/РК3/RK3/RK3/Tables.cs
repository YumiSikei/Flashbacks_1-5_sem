using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Data.SqlClient;
using System.Data.Linq.Mapping;

namespace RK
{
    [Table(Name = "RK.Bus")]
    public class Bus
    {

        [Column]
        public int ID { get; set; }

        [Column]
        public string BType { get; set; }

        [Column]
        public string Mark { get; set; }

        [Column]
        public string Num { get; set; }

        [Column]
        public string BusDriver { get; set; }

    }


    [Table(Name = "RK.Way")]
    public class Way
    {
        [Column]
        public int ID { get; set; }

        [Column]
        public int Num { get; set; }

        [Column]
        public int Bus { get; set; }

    }

}
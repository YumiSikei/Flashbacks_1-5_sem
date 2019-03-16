using System;
using System.Data;
using Microsoft.SqlServer.Server;
using System.Data.SqlTypes;
using System.Data.SqlClient;
using System.Collections;
using System.Diagnostics;
using System.Collections.ObjectModel;
using System.Text;

[Serializable]
[Microsoft.SqlServer.Server.SqlUserDefinedAggregate(Format.UserDefined,
IsInvariantToNulls = true,
IsInvariantToDuplicates = false,
IsInvariantToOrder = false,
MaxByteSize = 8000)]
public class AggrFunction : IBinarySerialize
{
    private Collection<int> num;
    private int result;

    public void Init()
    {
        num = new Collection<int>();
        result = -1;
    }

    public void Read(System.IO.BinaryReader reader)
    {
        this.result = reader.ReadInt32();
        int counter = reader.ReadInt32();

        num = new Collection<int>();

        for (int i = 0; i < counter; i++)
        {
            this.num.Add(reader.ReadInt32());
        }
    }

    public void Write(System.IO.BinaryWriter writer)
    {
        writer.Write(this.result);
        writer.Write(num.Count);

        foreach (int entry in num)
        {
            writer.Write(entry);
        }
    }
	
    public void Accumulate(int value)
    {
        num.Add(value);
    }

    public void Merge(AggrFunction other)
    {
        if (null != other.num && other.num.Count > 0)
        {
            foreach (int value in other.num)
            {
                num.Add(value);
            }
        }
    }

    public SqlInt32 Terminate()
    {
        Collection<int> repeated = new Collection<int>();

        foreach (int value in num)
        {
            int count = 0;

            for (int j = 0; j < num.Count; j++)
            {
                if (value.Equals(num[j]))
                {
                    count++;
                }
            }

            repeated.Add(count);
        }

        result = repeated[0];

        foreach (int value in repeated)
        {
            if (value < result)
            {
                result = value;
            }
        }

        return new SqlInt32(result);
    }

}
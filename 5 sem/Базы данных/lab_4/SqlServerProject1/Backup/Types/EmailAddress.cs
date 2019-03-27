using System;
using System.Data;
using System.Data.SqlClient;
using System.Data.SqlTypes;
using Microsoft.SqlServer.Server;
using System.Text.RegularExpressions;
using System.IO;

[Serializable]
[Microsoft.SqlServer.Server.SqlUserDefinedType(Format.UserDefined, IsByteOrdered = true, MaxByteSize = 8000)]
public struct EmailAddress : INullable, IBinarySerialize
{
    private string _value;
    /// <summary>
    /// The email address value.
    /// </summary>
    public string Value
    {
        get { return _value; }
        set { _value = value; }
    }

    /// <summary>
    /// The part of the email address before the @ sign.
    /// </summary>
    public string Prefix
    {
        get
        {
            string[] x = Value.Split('@');
            return x[0];
        }
    }

    /// <summary>
    /// The domain of the email address.
    /// </summary>
    public string Domain
    {
        get
        {
            string[] x = Value.Split('@');
            return x[1];
        }

    }

    public override string ToString()
    {
        return _value;
    }

    private bool _isNull;
    public bool IsNull
    {
        get
        {
            return _isNull;
        }
    }

    public static EmailAddress Null
    {
        get
        {
            EmailAddress h = new EmailAddress();
            h._isNull = true;
            return h;
        }
    }

    public static EmailAddress Parse(SqlString s)
    {
        if (s.IsNull)
            return Null;

        EmailAddress email = new EmailAddress();
        if (email.ValidateEmail(s))
        {
            email.Value = s.ToString();
            return email;
        }
        else
        {
            throw new SqlTypeException("The email " + s.ToString() + " was not in the proper format.");
        }
    }

    /// <summary>
    /// Validates the email being passed in.
    /// </summary>
    /// <param name="email"></param>
    /// <returns></returns>
    public bool ValidateEmail(SqlString email)
    {
        bool isValid = false;
        if (this.IsNull)
        {
            return true;
        }

        isValid = Regex.IsMatch(email.ToString(), @"^[\w-]+(?:\.[\w-]+)*@(?:[\w-]+\.)+[a-zA-Z]{2,7}$");
        if (isValid)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    public void Write(BinaryWriter w)
    {
        w.Write(_value);
    }

    public void Read(BinaryReader r)
    {
        _value = r.ReadString();
    }

}



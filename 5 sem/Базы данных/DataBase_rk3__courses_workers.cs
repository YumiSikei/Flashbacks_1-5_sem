#pragma warning disable 1591


namespace RK3
{
	using System.Data.Linq;
	using System.Data.Linq.Mapping;
	using System.Data;
	using System.Collections.Generic;
	using System.Reflection;
	using System.Linq;
	using System.Linq.Expressions;
	using System.ComponentModel;
	using System;
	
	
	[global::System.Data.Linq.Mapping.DatabaseAttribute(Name="RK3")]
	public partial class rk3dbDataContext : System.Data.Linq.DataContext
	{
		
		private static System.Data.Linq.Mapping.MappingSource mappingSource = new AttributeMappingSource();
		
    #region Определения метода расширяемости
    partial void OnCreated();
    partial void InsertCourses(Courses instance);
    partial void UpdateCourses(Courses instance);
    partial void DeleteCourses(Courses instance);
    partial void InsertWorkers(Workers instance);
    partial void UpdateWorkers(Workers instance);
    partial void DeleteWorkers(Workers instance);
    #endregion
		
		public rk3dbDataContext() : 
				base(global::RK3.Properties.Settings.Default.RK3ConnectionString, mappingSource)
		{
			OnCreated();
		}
		
		public rk3dbDataContext(string connection) : 
				base(connection, mappingSource)
		{
			OnCreated();
		}
		
		public rk3dbDataContext(System.Data.IDbConnection connection) : 
				base(connection, mappingSource)
		{
			OnCreated();
		}
		
		public rk3dbDataContext(string connection, System.Data.Linq.Mapping.MappingSource mappingSource) : 
				base(connection, mappingSource)
		{
			OnCreated();
		}
		
		public rk3dbDataContext(System.Data.IDbConnection connection, System.Data.Linq.Mapping.MappingSource mappingSource) : 
				base(connection, mappingSource)
		{
			OnCreated();
		}
		
		public System.Data.Linq.Table<Courses> Courses
		{
			get
			{
				return this.GetTable<Courses>();
			}
		}
		
		public System.Data.Linq.Table<Workers> Workers
		{
			get
			{
				return this.GetTable<Workers>();
			}
		}
	}
	
	[global::System.Data.Linq.Mapping.TableAttribute(Name="dbo.Courses")]
	public partial class Courses : INotifyPropertyChanging, INotifyPropertyChanged
	{
		
		private static PropertyChangingEventArgs emptyChangingEventArgs = new PropertyChangingEventArgs(String.Empty);
		
		private int _id;
		
		private int _id_Courses;
		
		private string @__course;
		
		private System.Nullable<System.DateTime> @__data;
		
		private string @__specialty;
		
		private System.Nullable<System.TimeSpan> @__time;
		
		private int @__CountOfParticipant;
		
    #region Определения метода расширяемости
    partial void OnLoaded();
    partial void OnValidate(System.Data.Linq.ChangeAction action);
    partial void OnCreated();
    partial void OnidChanging(int value);
    partial void OnidChanged();
    partial void Onid_CoursesChanging(int value);
    partial void Onid_CoursesChanged();
    partial void On_courseChanging(string value);
    partial void On_courseChanged();
    partial void On_dataChanging(System.Nullable<System.DateTime> value);
    partial void On_dataChanged();
    partial void On_specialtyChanging(string value);
    partial void On_specialtyChanged();
    partial void On_timeChanging(System.Nullable<System.TimeSpan> value);
    partial void On_timeChanged();
    partial void On_CountofParticipantChanging(System.Nullable<int> value);
    partial void On_CountofParticipantChanging();
    #endregion
		
		public Courses()
		{
			OnCreated();
		}
		
		[global::System.Data.Linq.Mapping.ColumnAttribute(Storage="_id", DbType="Int NOT NULL", IsPrimaryKey=true)]
		public int id
		{
			get
			{
				return this._id;
			}
			set
			{
				if ((this._id != value))
				{
					this.OnidChanging(value);
					this.SendPropertyChanging();
					this._id = value;
					this.SendPropertyChanged("id");
					this.OnidChanged();
				}
			}
		}
		
		[global::System.Data.Linq.Mapping.ColumnAttribute(Storage="_id_Courses", DbType="Int NOT NULL")]
		public int id_Courses
		{
			get
			{
				return this._id_Courses;
			}
			set
			{
				if ((this._id_Courses != value))
				{
					this.Onid_CoursesChanging(value);
					this.SendPropertyChanging();
					this._id_Courses = value;
					this.SendPropertyChanged("id_Courses");
					this.Onid_CoursesChanged();
				}
			}
		}
		
		[global::System.Data.Linq.Mapping.ColumnAttribute(Name="[_course]", Storage="__course", DbType="VarChar(50) NOT NULL")]
		public string _course
		{
			get
			{
				return this.@__course;
			}
			set
			{
				if ((this.@__course != value))
				{
					this.On_dataChanging(value);
					this.SendPropertyChanging();
					this.@__course = value;
					this.SendPropertyChanged("_course");
					this.On_courseChanged();
				}
			}
		}
		
		[global::System.Data.Linq.Mapping.ColumnAttribute(Name="[_data]", Storage="__data", DbType="Date")]
		public System.Nullable<System.DateTime> _data
		{
			get
			{
				return this.@__data;
			}
			set
			{
				if ((this.@__data != value))
				{
					this.On_dataChanging(value);
					this.SendPropertyChanging();
					this.@__data = value;
					this.SendPropertyChanged("_data");
					this.On_dataChanged();
				}
			}
		}
		
		[global::System.Data.Linq.Mapping.ColumnAttribute(Name="[_specialty]", Storage="__specialty", DbType="VarChar(50) NOT NULL")]
		public string _specialty
		{
			get
			{
				return this.@__specialty;
			}
			set
			{
				if ((this.@__specialty != value))
				{
					this.On_specialtyChanging(value);
					this.SendPropertyChanging();
					this.@__specialty = value;
					this.SendPropertyChanged("_specialty");
					this.On_specialtyChanged();
				}
			}
		}
		
		[global::System.Data.Linq.Mapping.ColumnAttribute(Name="[_time]", Storage="__time", DbType="Time")]
		public System.Nullable<System.TimeSpan> _time
		{
			get
			{
				return this.@__time;
			}
			set
			{
				if ((this.@__time != value))
				{
					this.On_timeChanging(value);
					this.SendPropertyChanging();
					this.@__time = value;
					this.SendPropertyChanged("_time");
					this.On_timeChanged();
				}
			}
		}
		
		[global::System.Data.Linq.Mapping.ColumnAttribute(Name="[_CountOfParticipant]", Storage="__CountOfParticipant", DbType="Int NOT NULL")]
		public int _CountOfParticipant
		{
			get
			{
				return this.@__CountOfParticipant;
			}
			set
			{
				if ((this.@__CountOfParticipant != value))
				{
					this.On_CountOfParticipantChanging(value);
					this.SendPropertyChanging();
					this.@__CountOfParticipant = value;
					this.SendPropertyChanged("_CountOfParticipant");
					this.On_CountOfParticipantChanged();
				}
			}
		}
		
		public event PropertyChangingEventHandler PropertyChanging;
		
		public event PropertyChangedEventHandler PropertyChanged;
		
		protected virtual void SendPropertyChanging()
		{
			if ((this.PropertyChanging != null))
			{
				this.PropertyChanging(this, emptyChangingEventArgs);
			}
		}
		
		protected virtual void SendPropertyChanged(String propertyName)
		{
			if ((this.PropertyChanged != null))
			{
				this.PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
			}
		}
	}
	
	[global::System.Data.Linq.Mapping.TableAttribute(Name="dbo.Workers")]
	public partial class Workers : INotifyPropertyChanging, INotifyPropertyChanged
	{
		
		private static PropertyChangingEventArgs emptyChangingEventArgs = new PropertyChangingEventArgs(String.Empty);
		
		private int _id;
		
		private string _fio;
		
		private System.Nullable<System.DateTime> _birthday;
		
		private string @__specialty;
		
		private System.Nullable<System.DateTime> _datalastqualification;
		
		private int _id_Courses;
		
    #region Определения метода расширяемости
    partial void OnLoaded();
    partial void OnValidate(System.Data.Linq.ChangeAction action);
    partial void OnCreated();
    partial void OnidChanging(int value);
    partial void OnidChanged();
    partial void OnfioChanging(string value);
    partial void OnfioChanged();
    partial void OnbirthdayChanging(System.Nullable<System.DateTime> value);
    partial void OnbirthdayChanged();
    partial void On_specialtyChanging(string value);
    partial void On_specialtyChanged();
    partial void On_datalastqualificationChanging(System.Nullable<System.DateTime> value);
    partial void On_datalastqualificationChanging();
	partial void Onid_CoursesChanging(int value);
    partial void Onid_CoursesChanged();
    #endregion
		
		public Workers()
		{
			OnCreated();
		}
		
		[global::System.Data.Linq.Mapping.ColumnAttribute(Storage="_id", DbType="Int NOT NULL", IsPrimaryKey=true)]
		public int id
		{
			get
			{
				return this._id;
			}
			set
			{
				if ((this._id != value))
				{
					this.OnidChanging(value);
					this.SendPropertyChanging();
					this._id = value;
					this.SendPropertyChanged("id");
					this.OnidChanged();
				}
			}
		}
		
		[global::System.Data.Linq.Mapping.ColumnAttribute(Storage="_fio", DbType="VarChar(50)")]
		public string fio
		{
			get
			{
				return this._fio;
			}
			set
			{
				if ((this._fio != value))
				{
					this.OnfioChanging(value);
					this.SendPropertyChanging();
					this._fio = value;
					this.SendPropertyChanged("fio");
					this.OnfioChanged();
				}
			}
		}
		
		[global::System.Data.Linq.Mapping.ColumnAttribute(Storage="_birthday", DbType="Date")]
		public System.Nullable<System.DateTime> birthday
		{
			get
			{
				return this._birthday;
			}
			set
			{
				if ((this._birthday != value))
				{
					this.OnbirthdayChanging(value);
					this.SendPropertyChanging();
					this._birthday = value;
					this.SendPropertyChanged("birthday");
					this.OnbirthdayChanged();
				}
			}
		}
		
		[global::System.Data.Linq.Mapping.ColumnAttribute(Name="[_specialty]", Storage="__specialty", DbType="VarChar(50) NOT NULL")]
		public string _specialty
		{
			get
			{
				return this.@__specialty;
			}
			set
			{
				if ((this.@__specialty != value))
				{
					this.On_specialtyChanging(value);
					this.SendPropertyChanging();
					this.@__specialty = value;
					this.SendPropertyChanged("_specialty");
					this.On_specialtyChanged();
				}
			}
		}
		
		[global::System.Data.Linq.Mapping.ColumnAttribute(Storage="_datalastqualification", DbType="Date")]
		public System.Nullable<System.DateTime> datalastqualification
		{
			get
			{
				return this._datalastqualification;
			}
			set
			{
				if ((this._datalastqualification != value))
				{
					this.On_datalastqualificationChanging(value);
					this.SendPropertyChanging();
					this._datalastqualification = value;
					this.SendPropertyChanged("datalastqualification");
					this.On_datalastqualificationChanged();
				}
			}
		}
		
		[global::System.Data.Linq.Mapping.ColumnAttribute(Storage="_id_Courses", DbType="Int NOT NULL")]
		public int id_Courses
		{
			get
			{
				return this._id_Courses;
			}
			set
			{
				if ((this._id_Courses != value))
				{
					this.Onid_CoursesChanging(value);
					this.SendPropertyChanging();
					this._id_Courses = value;
					this.SendPropertyChanged("id_Courses");
					this.Onid_CoursesChanged();
				}
			}
		}
		
		public event PropertyChangingEventHandler PropertyChanging;
		
		public event PropertyChangedEventHandler PropertyChanged;
		
		protected virtual void SendPropertyChanging()
		{
			if ((this.PropertyChanging != null))
			{
				this.PropertyChanging(this, emptyChangingEventArgs);
			}
		}
		
		protected virtual void SendPropertyChanged(String propertyName)
		{
			if ((this.PropertyChanged != null))
			{
				this.PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
			}
		}
	}
}
#pragma warning restore 1591

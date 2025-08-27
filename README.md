# 🏪 Departmental Store Management System

A comprehensive Python-based management system designed to streamline operations for departmental stores. This system efficiently handles product inventory, customer relationships, sales invoicing, and provides valuable data insights through visual analytics.

## ✨ Features

### 📦 Product Management
- **View** all products in inventory
- **Add** new products to the catalog
- **Remove** discontinued products
- **Modify** product details and pricing

### 👥 Customer Management
- **Maintain** customer database with full CRUD operations
- **Track** customer purchase history
- **Manage** customer contact information

### 🧾 Invoice System
- **Generate** detailed sales invoices
- **Automatic** stock level updates
- **Multiple** payment mode support
- **Complete** sales transaction records

### 📊 Data Analysis & Visualization
- **Product category-wise** inventory analysis (bar charts)
- **Payment mode** frequency analysis (line charts)
- **Real-time** business insights
- **Interactive** data visualizations

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | Python (VS Code) |
| **Backend** | MySQL |
| **Data Manipulation** | pandas |
| **Database Connectivity** | mysql-connector |
| **Data Visualization** | matplotlib |

## 🗃️ Database Schema

The system uses a MySQL database named `department` with the following tables:

### Products Table
| Field | Type | Constraints |
|-------|------|-------------|
| `ItemID` | VARCHAR(15) | PRIMARY KEY |
| `Item_Name` | VARCHAR(25) | |
| `Category` | VARCHAR(20) | |
| `Price` | FLOAT(5,2) | |
| `Units_Available` | INT | |

### Customer Table
| Field | Type | Constraints |
|-------|------|-------------|
| `CustID` | VARCHAR(10) | PRIMARY KEY |
| `First_Name` | VARCHAR(15) | |
| `Last_Name` | VARCHAR(15) | |
| `Phone` | BIGINT | |
| `Email` | VARCHAR(25) | |

### Invoice Table
| Field | Type | Constraints |
|-------|------|-------------|
| `InvoiceNO` | VARCHAR(10) | PRIMARY KEY |
| `CustID` | VARCHAR(10) | |
| `Sale_Date` | DATE | |
| `Payment_Mode` | VARCHAR(20) | |

### Invoice Line Item Table
| Field | Type | Constraints |
|-------|------|-------------|
| `InvoiceNO` | VARCHAR(10) | |
| `ItemID` | VARCHAR(10) | |
| `Quantity` | INT | |
| `Amount` | INT | |

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd departmental-store-management
   ```

2. **Install required dependencies**
   ```bash
   pip install pandas mysql-connector-python matplotlib
   ```

3. **Set up MySQL database**
   - Create a database named `department`
   - Execute the table creation scripts based on the schema above

4. **Configure database connection**
   ```python
   # Update connection details in the code
   conn = mycon.connect(host='localhost', user='root', 
                       password='your_password', database='department', port=3306)
   ```

## 💻 Usage

Run the main Python script to start the application:

```bash
python departmental_store.py
```

### 🎯 Main Menu Options

1. **📦 Products Management**
   - View all products
   - Add new products
   - Remove products
   - Modify product details

2. **👥 Customer Management**
   - View all customers
   - Add new customers
   - Remove customers
   - Modify customer details

3. **🧾 Invoice Management**
   - View customer invoices
   - Create new invoices
   - Delete existing invoices

4. **📊 Data Analysis**
   - Product inventory analysis (bar chart)
   - Payment mode analysis (line chart)

5. **🚪 Exit** - Close the application

## ⭐ Key Features

- **✅ Input Validation**: Comprehensive validation including phone number verification and duplicate ID checks
- **🔄 Automatic Stock Management**: Real-time inventory updates when processing invoices
- **📈 Data Visualization**: Built-in analytics with matplotlib charts for business intelligence
- **🎨 User-Friendly Interface**: Intuitive console-based menu system for easy navigation
- **🔒 Data Integrity**: Foreign key constraints and transaction management

## 📸 Sample Outputs

The application features clean, formatted output displays for all operations including:
- Tabular product listings
- Customer information displays
- Detailed invoice printouts
- Interactive data visualizations

## 🤝 Contributing

We welcome contributions! Feel free to:

1. Fork this project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**⭐ Star this repo if you found it helpful!**

For questions or support, please open an issue in the GitHub repository.

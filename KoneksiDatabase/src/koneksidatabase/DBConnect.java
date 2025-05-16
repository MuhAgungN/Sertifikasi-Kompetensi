/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package koneksidatabase;

import com.mysql.jdbc.PreparedStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Calendar;

/**
 *
 * @author MuhAgungN173
 */
public class DBConnect {

    private Connection con;
    private Statement st;
    private ResultSet rs;

    public DBConnect() throws SQLException {
        String url = "jdbc:mysql://localhost:3306/";
        String dbName = "ref_bank";
        String driver = "com.mysql.jdbc.Driver";
        String userName = "root";
        String password = "";
        try {
            Class.forName(driver).newInstance();
            con = DriverManager.getConnection(url + dbName, userName,
                    password);
            st = (Statement) con.createStatement();
            System.out.println("Koneksi Sukses");
        } catch (ClassNotFoundException | InstantiationException | IllegalAccessException | SQLException ex) {
            System.out.println("Error: " + ex);
        }
    }

    public int getCountBank() {
        int rowCount = 0;
        try {
            String q = "select count(*) as jum from ref_bank";
            rs = st.executeQuery(q);
            rs.next();
            rowCount = rs.getInt("jum");
        } catch (Exception ex) {
            System.out.println("Error: " + ex);
        }
        return rowCount;
    }

    public Object[][] getDataBank() {
        Object[][] row = new Object[1000][3];
        try {
            String query = "select * from ref_bank";
            rs = st.executeQuery(query);
            int i = 0;
            while (rs.next()) {
                row[i][0] = rs.getString("kode");
                row[i][1] = rs.getString("nama");
                row[i][2] = rs.getString("deskripsi");
                i++;
            }
        } catch (Exception ex) {
            System.out.println("Error: " + ex);
        }
        return row;
    }

    public void setDataBank(String kode, String nama, String deskripsi) {
        try {
            String q = "select max(id) as maks from ref_bank";
            rs = st.executeQuery(q);
            rs.next();
            int rowCount = rs.getInt("maks");
            rowCount = rowCount + 1;

            Calendar calendar = Calendar.getInstance();
            java.sql.Timestamp lastUpdate = new java.sql.Timestamp(calendar.getTime().getTime());

            String query = "INSERT INTO ref_bank (id, kode, nama, deskripsi, lastUpdate, userUpdate) VALUES (?, ?, ?, ?, ?, ?)";
            PreparedStatement preparedStmt = (PreparedStatement) con.prepareStatement(query);
            preparedStmt.setInt(1, rowCount);
            preparedStmt.setString(2, kode);
            preparedStmt.setString(3, nama);
            preparedStmt.setString(4, deskripsi);
            preparedStmt.setTimestamp(5, lastUpdate);
            preparedStmt.setInt(6, 1);

            preparedStmt.execute();

            if (!con.getAutoCommit()) {
                con.commit(); // Commit jika autoCommit = false
            }

            System.out.println("Data berhasil disimpan ke database");

        } catch (Exception ex) {
            ex.printStackTrace(); // Tampilkan error lengkap
        }
    }


    public void deleteBank(int kd) {
        try {
            String query = " delete from ref_bank where kode = ?";
            PreparedStatement preparedStmt;
            preparedStmt = (PreparedStatement) con.prepareStatement(query);
            preparedStmt.setInt(1, kd);
            preparedStmt.execute();
            preparedStmt.close();
        } catch (Exception ex) {
            System.out.println("Error: " + ex);
        }
    }


    public void updateBank(String nama, String deskripsi, String kode) {
        try {
            Calendar calendar = Calendar.getInstance();
            java.sql.Timestamp lastUpdate = new java.sql.Timestamp(calendar.getTime().getTime());
            String query = " update ref_bank set nama = ?, deskripsi = ? , lastUpdate =  ? where  kode =  ?";
            PreparedStatement preparedStmt;
            preparedStmt = (PreparedStatement) con.prepareStatement(query);
            preparedStmt.setString(1, nama);
            preparedStmt.setString(2, deskripsi);
            preparedStmt.setTimestamp(3, lastUpdate);
            preparedStmt.setString(4, kode);
            preparedStmt.execute();
            preparedStmt.close();
        } catch (Exception ex) {
            System.out.println("Error: " + ex);
        }
    }
}

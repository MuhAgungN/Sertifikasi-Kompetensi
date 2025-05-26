/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package kalkulator;

import java.util.Scanner;

/**
 *
 * @author MuhAgungN173
 */
public class Kalkulator {

    public static void tampilkanSpesifikasi() {
        System.out.println("Program Kalkulator Sederhana versi 1.0");
        System.out.println("Fungsi: Penjumlahan, Pengurangan, Perkalian, Pembagian");
        System.out.println("Dibuat sesuai prinsip OOP dan Best Practices\n");
    }
    
    public static void main(String[] args) {
        tampilkanSpesifikasi();

        try (Scanner input = new Scanner(System.in)) {
            boolean lanjut = true;
            
            while (lanjut) {
                System.out.println("Pilih operasi:");
                System.out.println("1. Tambah");
                System.out.println("2. Kurang");
                System.out.println("3. Kali");
                System.out.println("4. Bagi");
                System.out.println("5. Keluar");
                System.out.print("Pilihan: ");
                
                int pilihan = input.nextInt();
                
                if (pilihan == 5) {
                    System.out.println("Keluar dari program.");
                    break;
                }
                
                System.out.print("Masukkan angka pertama: ");
                double angka1 = input.nextDouble();
                
                System.out.print("Masukkan angka kedua: ");
                double angka2 = input.nextDouble();
                
                double hasil = 0;
                boolean valid = true;
                
                switch (pilihan) {
                    case 1:
                        hasil = tambah(angka1, angka2);
                        break;
                    case 2:
                        hasil = kurang(angka1, angka2);
                        break;
                    case 3:
                        hasil = kali(angka1, angka2);
                        break;
                    case 4:
                        if (angka2 != 0) {
                            hasil = bagi(angka1, angka2);
                        } else {
                            System.out.println("❌ Pembagian dengan nol tidak diperbolehkan!");
                            valid = false;
                        }
                        break;
                    default:
                        System.out.println("❌ Pilihan tidak valid!");
                        valid = false;
                }
                
                if (valid) {
                    System.out.println("Hasil: " + hasil);
                }
                
                System.out.println();
            }
        }
    }

    // Implementasi fungsi terstruktur
    public static double tambah(double a, double b) {
        return a + b;
    }

    public static double kurang(double a, double b) {
        return a - b;
    }

    public static double kali(double a, double b) {
        return a * b;
    }

    public static double bagi(double a, double b) {
        return a / b;
    }
}

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package gametebakangka;

import java.util.Random;
import java.util.Scanner;
/**
 *
 * @author user
 */
public class GameTebakAngka {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Random r = new Random();
        int rand = r.nextInt(100);
//        System.out.println("Angka yang komputer miliki adalah " + rand);
        Scanner input = new Scanner(System.in);
        System.out.println("Main Tebak angka antara 1 - 100");

        while (true) {
            System.out.print("Masukkan Angka Tebakan Anda : ");
            int x = input.nextInt();
            if (rand > x) {
                System.out.println("Angka Terlalu Kecil");
            } 
            
            if (rand < x) {
                System.out.println("Angka Terlalu Besar");
            }            
            
            if (rand == x) {
                System.out.println("Tebakan Anda benar " + x);
                break;
            } 
        }
        
        
    }
    
}

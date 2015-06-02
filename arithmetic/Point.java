package com.zzm.interview;

public class Point {
    private int x;
    private int y;
    private int shortest;

    public Point() {
    }

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public int getShortest() {
        return shortest;
    }

    public void addShortest(Point point) {
        this.shortest = point.getShortest() + 1;
    }
}

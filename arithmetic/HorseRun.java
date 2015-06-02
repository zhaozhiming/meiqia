package com.zzm.interview;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class HourseRun {
    private static final int MAX_SIZE = 8;
    private static final int MIN_SIZE = 1;
    private Point start;
    private Point end;

    private List<Point> direction = new ArrayList<>();
    private LinkedList<Point> unVisitedPoint = new LinkedList<>();
    private int[][] markVisited = new int[9][9];

    public HourseRun(Point start, Point end) {
        this.start = start;
        this.end = end;
        init();
    }

    public void init() {
        direction.add(new Point(2, 1)); //right up horizontal
        direction.add(new Point(2, -1)); //right down horizontal
        direction.add(new Point(1, -2)); //right down vertical
        direction.add(new Point(-1, -2)); //left down vertical
        direction.add(new Point(-2, -1)); //left down horizontal
        direction.add(new Point(-2, 1)); //left up horizontal
        direction.add(new Point(-1, 2)); //left up vertical
        direction.add(new Point(1, 2)); //right up vertical
    }

    private int bfs() {
        Point current = new Point();
        while (!unVisitedPoint.isEmpty()) {
            current = unVisitedPoint.poll();
            markVisited[current.getX()][current.getY()] = 1;

            if (current.getX() == end.getX() && current.getY() == end.getY()) {
                break;
            }

            for(Point aDirection: direction) {
                Point next = new Point(current.getX() + aDirection.getX(), current.getY() + aDirection.getY());
                next.addShortest(current);

                if (next.getX() < MIN_SIZE || next.getX() > MAX_SIZE || next.getY() < MIN_SIZE || next.getY() > MAX_SIZE) {
                    continue;
                }

                if (markVisited[next.getX()][next.getY()] == 0) {
                    unVisitedPoint.add(next);
                }
            }

        }
        return current.getShortest();
    }

    public int find() {
        this.unVisitedPoint.add(start);
        return bfs();
    }


}

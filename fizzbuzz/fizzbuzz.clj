(defn multiple? [x n]
  (= 0 (mod x n)))

(defn fb-el [a b i]
  (if (multiple? i a)
    (if (multiple? i b) "FB" "F")
    (if (multiple? i b) "B" i)))

(defn fizzbuzz [a b n]
  (apply str (interpose " " (map #(fb-el a b %) (range 1 (inc n))))))

(with-open [rdr (clojure.java.io/reader (first *command-line-args*))]
  (doseq [line (remove empty? (line-seq rdr))]
    (println 
      (apply fizzbuzz (map #(Integer. %) (rest (re-find #"(\d+)\s+(\d+)\s+(\d+)\n?" line)))))))

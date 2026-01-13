/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_sort_algo.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/10 23:34:43 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/10 23:34:45 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_sort_three(td_list **stack)
{
	int	first;
	int	second;
	int	third;

	first = *(int *)(*stack)->content;
	second = *(int *)(*stack)->next->content;
	third = *(int *)(*stack)->next->next->content;
	if (first > second && second < third && first < third)
		ft_sa(stack); // sa
	else if (first > second && second > third)
	{
		ft_sa(stack);  // sa
		ft_rra(stack); // rra
	}
	else if (first > second && second < third && first > third)
		ft_rra(stack); // rra
	else if (first < second && second > third && first < third)
	{
		ft_sa(stack); // sa
		ft_ra(stack); // ra
	}
	else if (first < second && second > third && first > third)
		ft_ra(stack); // ra
}

void	ft_sort_four(td_list **stack_a, td_list **stack_b)
{
	int	pos;

	if (ft_is_sorted(*stack_a) == 1)
		return ;
	pos = ft_find_min(*stack_a);
	if (pos == 1)
		ft_ra(stack_a);
	else if (pos == 2)
	{
		ft_ra(stack_a);
		ft_ra(stack_a);
	}
	else if (pos == 3)
		ft_rra(stack_a);
	ft_pb(stack_a, stack_b);
	ft_sort_three(stack_a);
	ft_pa(stack_a, stack_b);
}

void	ft_sort_five(td_list **stack_a, td_list **stack_b)
{
	int	pos;

	if (ft_is_sorted(*stack_a) == 1)
		return ;
	pos = ft_find_min(*stack_a);
	if (pos == 1)
		ft_ra(stack_a);
	else if (pos == 2)
	{
		ft_ra(stack_a);
		ft_ra(stack_a);
	}
	else if (pos == 3)
	{
		ft_rra(stack_a);
		ft_rra(stack_a);
	}
	else if (pos == 4)
		ft_rra(stack_a);
	ft_pb(stack_a, stack_b);
	ft_sort_four(stack_a, stack_b);
	ft_pa(stack_a, stack_b);
}

void	ft_sort_n(td_list **stack_a, td_list **stack_b, int size)
{
    int *lis;
    lis = ft_find_lis(stack_a, size);
	ft_printf("LIS array obtained.\n");
	ft_push_non_lis(stack_a, stack_b, lis, size);
    //ft_sort_remaining(stack_a, stack_b);
    //ft_final_rotate(stack_a);

}

void	ft_sort_stack(td_list **stack_a, td_list **stack_b)
{
	int	size;

	size = ft_lstd_size(*stack_a);
	if (size <= 1 || ft_is_sorted(*stack_a))
		return ;
	else if (size == 2)
	{
		if (*(int *)(*stack_a)->content > *(int *)(*stack_a)->next->content)
			ft_sa(stack_a);
	}
	else if (size == 3)
		ft_sort_three(stack_a);
	else if (size == 4)
	{
		ft_sort_four(stack_a, stack_b);
	}
	else if (size == 5)
	{
		ft_sort_five(stack_a, stack_b);
	}
	else
	{
		ft_sort_n(stack_a, stack_b, size);
	}
	// Further sorting algorithms for larger sizes can be implemented here
}
